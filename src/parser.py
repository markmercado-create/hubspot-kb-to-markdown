"""
File-type dispatcher — routes input files to the correct reader.
Supported formats: .csv, .xls, .xlsx, .html, .htm
"""

import logging
from pathlib import Path

from .models import Article
from .readers import csv_reader, excel_reader, html_reader

logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = {".csv", ".xls", ".xlsx", ".html", ".htm"}


def load_articles(file_path: Path) -> list[Article]:
    """
    Load articles from any supported input file.

    Dispatches to the correct reader based on file extension.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if the file type is not supported.
    """
    ext = file_path.suffix.lower()

    if ext == ".csv":
        return csv_reader.load(file_path)

    if ext in {".xls", ".xlsx"}:
        return excel_reader.load(file_path)

    if ext in {".html", ".htm"}:
        return html_reader.load(file_path)

    raise ValueError(
        f"Unsupported file type: '{ext}'. "
        f"Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
    )
