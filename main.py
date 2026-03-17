"""
HubSpot Knowledge Base → Markdown Converter
============================================
Entry point. Run with:

    python main.py                          # converts all CSVs in input/
    python main.py --file input/export.csv  # converts a specific file
    python main.py --help                   # show usage

All configurable paths come from the .env file (see .env.example).
"""

import argparse
import logging
import sys
from pathlib import Path

from src.config import INPUT_DIR, OUTPUT_DIR
from src.converter import convert_all
from src.parser import load_articles

logger = logging.getLogger(__name__)


def _collect_csv_files(file_arg: str | None) -> list[Path]:
    """Return the list of CSV files to process based on CLI input."""
    if file_arg:
        path = Path(file_arg)
        if not path.exists():
            logger.error("File not found: %s", path)
            sys.exit(1)
        if path.suffix.lower() != ".csv":
            logger.error("Expected a .csv file, got: %s", path)
            sys.exit(1)
        return [path]

    if not INPUT_DIR.exists():
        logger.error(
            "Input directory does not exist: %s\n"
            "Create it and place your HubSpot CSV export inside.",
            INPUT_DIR,
        )
        sys.exit(1)

    csv_files = sorted(INPUT_DIR.glob("*.csv"))
    if not csv_files:
        logger.error(
            "No .csv files found in %s\n"
            "Export your Knowledge Base from HubSpot and place the CSV there.",
            INPUT_DIR,
        )
        sys.exit(1)

    return csv_files


def run(file_arg: str | None = None, output_arg: str | None = None) -> int:
    """
    Main conversion flow.

    Returns:
        Exit code (0 = success, 1 = partial/full failure).
    """
    output_dir = Path(output_arg) if output_arg else OUTPUT_DIR
    csv_files = _collect_csv_files(file_arg)

    total_written: list[Path] = []
    total_failed = 0

    for csv_path in csv_files:
        logger.info("--- Processing: %s ---", csv_path.name)
        try:
            articles = load_articles(csv_path)
        except (FileNotFoundError, ValueError) as exc:
            logger.error("Could not load '%s': %s", csv_path.name, exc)
            total_failed += 1
            continue

        written = convert_all(articles, output_dir)
        total_written.extend(written)

    sep = "-" * 50
    print(f"\n{sep}")
    print(f"  Total files written : {len(total_written)}")
    print(f"  Output folder       : {output_dir.resolve()}")
    print(f"{sep}\n")

    return 0 if total_written else 1


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="main.py",
        description="Convert HubSpot Knowledge Base CSV exports to Markdown files.",
    )
    p.add_argument(
        "--file", "-f",
        metavar="PATH",
        help="Path to a specific CSV file. Defaults to all CSVs in the input/ folder.",
    )
    p.add_argument(
        "--output", "-o",
        metavar="DIR",
        help="Override the output directory (defaults to OUTPUT_DIR in .env).",
    )
    return p


if __name__ == "__main__":
    args = _build_parser().parse_args()
    sys.exit(run(file_arg=args.file, output_arg=args.output))
