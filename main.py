"""
HubSpot Knowledge Base -> Markdown Converter
=============================================
Converts CSV, Excel (.xls/.xlsx), or HTML files into Markdown.
Media files (images, videos, documents) are downloaded to a local media_files/ folder.

Usage:
    python main.py                          # converts all supported files in input/
    python main.py --file export.csv        # specific CSV
    python main.py --file article.html      # specific HTML file
    python main.py --file data.xlsx         # specific Excel file
    python main.py --no-media               # skip media downloading
    python main.py --help
"""

import argparse
import logging
import sys
from pathlib import Path

from src.config import INPUT_DIR, MEDIA_DIR, OUTPUT_DIR, SUPPORTED_EXTENSIONS
from src.converter import convert_all
from src.parser import load_articles

logger = logging.getLogger(__name__)


def _collect_input_files(file_arg: str | None) -> list[Path]:
    """Return the list of input files to process."""
    if file_arg:
        path = Path(file_arg)
        if not path.exists():
            logger.error("File not found: %s", path)
            sys.exit(1)
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            logger.error(
                "Unsupported file type '%s'. Supported: %s",
                path.suffix,
                ", ".join(sorted(SUPPORTED_EXTENSIONS)),
            )
            sys.exit(1)
        return [path]

    if not INPUT_DIR.exists():
        logger.error(
            "Input directory not found: %s\n"
            "Create it and place your export file(s) inside.",
            INPUT_DIR,
        )
        sys.exit(1)

    files: list[Path] = []
    for ext in SUPPORTED_EXTENSIONS:
        files.extend(INPUT_DIR.glob(f"*{ext}"))

    files = sorted(set(files))

    if not files:
        logger.error(
            "No supported files found in %s\n"
            "Supported formats: %s",
            INPUT_DIR,
            ", ".join(sorted(SUPPORTED_EXTENSIONS)),
        )
        sys.exit(1)

    return files


def run(
    file_arg: str | None = None,
    output_arg: str | None = None,
    media_arg: str | None = None,
    no_media: bool = False,
) -> int:
    """Main conversion flow. Returns 0 on success, 1 on failure."""
    import src.config as cfg

    output_dir = Path(output_arg) if output_arg else OUTPUT_DIR
    media_dir = Path(media_arg) if media_arg else MEDIA_DIR

    # Allow --no-media to override config at runtime
    if no_media:
        cfg.DOWNLOAD_MEDIA = False

    input_files = _collect_input_files(file_arg)
    total_written: list[Path] = []

    for input_path in input_files:
        logger.info("--- Processing: %s ---", input_path.name)
        try:
            articles = load_articles(input_path)
        except (FileNotFoundError, ValueError) as exc:
            logger.error("Could not load '%s': %s", input_path.name, exc)
            continue

        written = convert_all(articles, output_dir, media_dir)
        total_written.extend(written)

    sep = "-" * 50
    print(f"\n{sep}")
    print(f"  Input format(s)     : {', '.join(sorted({f.suffix for f in input_files}))}")
    print(f"  Total files written : {len(total_written)}")
    print(f"  Output folder       : {output_dir.resolve()}")
    print(f"  Media folder        : {media_dir.resolve()}")
    print(f"{sep}\n")

    return 0 if total_written else 1


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="main.py",
        description=(
            "Convert HubSpot Knowledge Base exports to Markdown.\n"
            "Supports: CSV (.csv), Excel (.xls, .xlsx), HTML (.html, .htm)"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--file", "-f", metavar="PATH",
        help="Path to a specific input file. Defaults to all supported files in input/.",
    )
    p.add_argument(
        "--output", "-o", metavar="DIR",
        help="Override the output directory (default: OUTPUT_DIR in .env).",
    )
    p.add_argument(
        "--media", "-m", metavar="DIR",
        help="Override the media download directory (default: MEDIA_DIR in .env).",
    )
    p.add_argument(
        "--no-media", action="store_true",
        help="Skip downloading media files (images, videos, documents).",
    )
    return p


if __name__ == "__main__":
    args = _build_parser().parse_args()
    sys.exit(run(
        file_arg=args.file,
        output_arg=args.output,
        media_arg=args.media,
        no_media=args.no_media,
    ))
