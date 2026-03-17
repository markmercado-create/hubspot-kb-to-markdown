"""
Shared helpers for detecting and mapping tabular column names.
Used by CSV and Excel readers.
"""

import logging
from typing import Optional

import pandas as pd

from .config import COLUMN_CANDIDATES

logger = logging.getLogger(__name__)


def detect_column(df_columns: list[str], candidates: list[str]) -> Optional[str]:
    """Return the first candidate column that exists in df_columns (case-insensitive)."""
    normalised = {c.strip().lower(): c for c in df_columns}
    for candidate in candidates:
        if candidate.lower() in normalised:
            return normalised[candidate.lower()]
    return None


def build_column_map(df_columns: list[str]) -> dict[str, Optional[str]]:
    """Map logical field names to the actual column names found in the file."""
    col_map: dict[str, Optional[str]] = {}
    for field_name, candidates in COLUMN_CANDIDATES.items():
        found = detect_column(df_columns, candidates)
        if found:
            logger.debug("Field '%s' -> column '%s'", field_name, found)
        else:
            logger.warning("Field '%s' not found. Checked: %s", field_name, candidates)
        col_map[field_name] = found
    return col_map


def safe_str(value) -> str:
    """Convert a cell value to string, treating NaN/None as empty string."""
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass
    return str(value).strip() if value is not None else ""
