"""
Central configuration loaded from environment variables / .env file.
All runtime-configurable values must originate here — never hardcoded.
"""

import logging
import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env from the project root (one level up from src/)
_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")


def _resolve(path_str: str) -> Path:
    """Return an absolute path; relative paths are resolved from the project root."""
    p = Path(path_str)
    return p if p.is_absolute() else (_ROOT / p)


INPUT_DIR: Path = _resolve(os.getenv("INPUT_DIR", "input"))
OUTPUT_DIR: Path = _resolve(os.getenv("OUTPUT_DIR", "output"))
USE_DATED_SUBFOLDER: bool = os.getenv("USE_DATED_SUBFOLDER", "false").lower() == "true"
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()

# Known HubSpot CSV column names, in priority order.
# The parser will use the first matching column it finds in the CSV.
# Covers both the real HubSpot export format and any custom variations.
COLUMN_CANDIDATES = {
    "title":         ["article title", "article_title", "title", "name"],
    "body":          ["article body", "article_body", "body", "content", "html", "body html", "body_html"],
    "category":      ["category", "category name", "category_name", "section"],
    "subcategory":   ["subcategory", "sub-category", "sub_category"],
    "url":           ["article url", "article_url", "url", "link", "public url", "public_url"],
    "status":        ["status", "state", "publish state", "publish_state"],
    "language":      ["article language", "article_language", "language", "locale", "lang"],
    "subtitle":      ["article subtitle", "article_subtitle", "subtitle"],
    "keywords":      ["keywords", "tags", "keyword"],
    "modified_date": ["last modified date", "last_modified_date", "updated at", "updated_at", "modified date"],
    "archived":      ["archived", "is archived", "is_archived"],
    "kb_name":       ["knowledge base name", "knowledge_base_name", "kb name", "kb_name"],
}

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
