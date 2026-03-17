"""
Reader for Excel (.xls / .xlsx) exports of HubSpot Knowledge Base content.
Expects the same column structure as the CSV export.
"""

import logging
from pathlib import Path

import pandas as pd

from ..column_utils import build_column_map, safe_str
from ..models import Article

logger = logging.getLogger(__name__)

_ENGINES = {".xlsx": "openpyxl", ".xls": "xlrd"}


def load(excel_path: Path) -> list[Article]:
    """
    Read a HubSpot KB Excel export and return a list of Article objects.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if the file extension is unsupported or columns cannot be detected.
    """
    if not excel_path.exists():
        raise FileNotFoundError(f"File not found: {excel_path}")

    ext = excel_path.suffix.lower()
    engine = _ENGINES.get(ext)
    if not engine:
        raise ValueError(f"Unsupported Excel format: '{ext}'. Use .xls or .xlsx")

    logger.info("Reading Excel (%s): %s", ext, excel_path.name)

    try:
        df = pd.read_excel(excel_path, dtype=str, engine=engine, keep_default_na=True)
    except Exception as exc:
        raise ValueError(f"Could not read Excel file '{excel_path.name}': {exc}") from exc

    logger.info("Loaded %d rows, %d columns", len(df), len(df.columns))

    col_map = build_column_map(list(df.columns))

    if not col_map.get("title") and not col_map.get("body"):
        raise ValueError(
            f"Could not detect title or body columns in '{excel_path.name}'. "
            "Ensure it follows the HubSpot KB export column structure."
        )

    articles: list[Article] = []
    skipped = 0

    for idx, row in df.iterrows():
        title = safe_str(row[col_map["title"]]) if col_map["title"] else ""
        body = safe_str(row[col_map["body"]]) if col_map["body"] else ""

        if not title and not body:
            skipped += 1
            continue

        def _col(field_name: str) -> str:
            col = col_map.get(field_name)
            return safe_str(row[col]) if col else ""

        articles.append(Article(
            title=title or f"Untitled_{idx}",
            body_html=body,
            category=_col("category"),
            subcategory=_col("subcategory"),
            url=_col("url"),
            status=_col("status"),
            language=_col("language"),
            subtitle=_col("subtitle"),
            keywords=_col("keywords"),
            modified_date=_col("modified_date"),
            archived=_col("archived"),
            kb_name=_col("kb_name"),
            raw=row.to_dict(),
        ))

    if skipped:
        logger.warning("Skipped %d empty rows.", skipped)

    logger.info("Parsed %d articles from Excel.", len(articles))
    return articles
