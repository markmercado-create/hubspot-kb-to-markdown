"""
CSV parser for HubSpot Knowledge Base exports.

HubSpot does not guarantee fixed column names across exports, so this module
detects which columns are present and maps them to a normalised Article schema.
"""

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import pandas as pd

from .config import COLUMN_CANDIDATES

logger = logging.getLogger(__name__)


@dataclass
class Article:
    """Normalised representation of a single KB article row."""

    title: str
    body_html: str
    category: str = ""
    subcategory: str = ""
    url: str = ""
    status: str = ""
    language: str = ""
    subtitle: str = ""
    keywords: str = ""
    modified_date: str = ""
    archived: str = ""
    kb_name: str = ""
    raw: dict = field(default_factory=dict)


def _detect_column(df_columns: list[str], candidates: list[str]) -> Optional[str]:
    """Return the first candidate column name that exists in the CSV (case-insensitive)."""
    normalised = {c.strip().lower(): c for c in df_columns}
    for candidate in candidates:
        if candidate.lower() in normalised:
            return normalised[candidate.lower()]
    return None


def _build_column_map(df_columns: list[str]) -> dict[str, Optional[str]]:
    """Map logical field names to the actual column names found in the CSV."""
    col_map: dict[str, Optional[str]] = {}
    for field_name, candidates in COLUMN_CANDIDATES.items():
        found = _detect_column(df_columns, candidates)
        if found:
            logger.debug("Field '%s' mapped to CSV column '%s'", field_name, found)
        else:
            logger.warning(
                "Field '%s' not found in CSV. Checked: %s", field_name, candidates
            )
        col_map[field_name] = found
    return col_map


def _safe_str(value) -> str:
    """Convert a cell value to a string, treating NaN/None as empty string."""
    if pd.isna(value):
        return ""
    return str(value).strip()


def load_articles(csv_path: Path) -> list[Article]:
    """
    Read a HubSpot KB CSV export and return a list of Article objects.

    Raises:
        FileNotFoundError: if the CSV does not exist.
        ValueError: if neither a title nor a body column can be detected.
    """
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    logger.info("Reading CSV: %s", csv_path)
    df = pd.read_csv(csv_path, dtype=str, keep_default_na=True)
    logger.info("Loaded %d rows, %d columns", len(df), len(df.columns))
    logger.debug("CSV columns: %s", list(df.columns))

    col_map = _build_column_map(list(df.columns))

    if not col_map.get("title") and not col_map.get("body"):
        raise ValueError(
            "Could not detect a title or body column in the CSV. "
            "Please check the file is a valid HubSpot KB export."
        )

    articles: list[Article] = []
    skipped = 0

    for idx, row in df.iterrows():
        title = _safe_str(row[col_map["title"]]) if col_map["title"] else f"Article_{idx}"
        body = _safe_str(row[col_map["body"]]) if col_map["body"] else ""

        if not title and not body:
            skipped += 1
            continue

        def _col(field_name: str) -> str:
            col = col_map.get(field_name)
            return _safe_str(row[col]) if col else ""

        articles.append(
            Article(
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
            )
        )

    if skipped:
        logger.warning("Skipped %d empty rows.", skipped)

    logger.info("Parsed %d articles from CSV.", len(articles))
    return articles
