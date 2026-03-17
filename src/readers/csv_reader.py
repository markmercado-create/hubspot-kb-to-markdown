"""
Reader for HubSpot Knowledge Base CSV exports.
"""

import logging
from pathlib import Path

import pandas as pd

from ..column_utils import build_column_map, safe_str
from ..models import Article

logger = logging.getLogger(__name__)


def load(csv_path: Path) -> list[Article]:
    """
    Read a HubSpot KB CSV export and return a list of Article objects.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if neither a title nor body column can be detected.
    """
    if not csv_path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")

    logger.info("Reading CSV: %s", csv_path.name)
    df = pd.read_csv(csv_path, dtype=str, keep_default_na=True)
    logger.info("Loaded %d rows, %d columns", len(df), len(df.columns))

    return _df_to_articles(df, csv_path.name)


def _df_to_articles(df: pd.DataFrame, source_name: str) -> list[Article]:
    col_map = build_column_map(list(df.columns))

    if not col_map.get("title") and not col_map.get("body"):
        raise ValueError(
            f"Could not detect title or body columns in '{source_name}'. "
            "Ensure it is a valid HubSpot KB export."
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

    logger.info("Parsed %d articles from CSV.", len(articles))
    return articles
