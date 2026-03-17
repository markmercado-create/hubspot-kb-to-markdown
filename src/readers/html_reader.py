"""
Reader for standalone HTML files (e.g. individual articles exported from HubSpot
or saved from a browser). Each HTML file is treated as one article.
"""

import logging
import re
from pathlib import Path

from bs4 import BeautifulSoup

from ..models import Article

logger = logging.getLogger(__name__)


def load(html_path: Path) -> list[Article]:
    """
    Parse a single HTML file and return it as a one-item list of Article objects.

    Raises:
        FileNotFoundError: if the file does not exist.
    """
    if not html_path.exists():
        raise FileNotFoundError(f"File not found: {html_path}")

    logger.info("Reading HTML: %s", html_path.name)
    raw_html = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw_html, "html.parser")

    title = _extract_title(soup, html_path)
    body_html = _extract_body(soup)
    language = _extract_meta(soup, ["lang", "language", "og:locale"]) or ""
    keywords = _extract_meta(soup, ["keywords"]) or ""
    description = _extract_meta(soup, ["description", "og:description"]) or ""
    url = _extract_meta(soup, ["og:url", "canonical"]) or ""

    article = Article(
        title=title,
        body_html=body_html,
        subtitle=description,
        keywords=keywords,
        url=url,
        language=language,
    )

    logger.info("Parsed 1 article from HTML: '%s'", title)
    return [article]


def load_directory(directory: Path) -> list[Article]:
    """Load all .html / .htm files from a directory as individual articles."""
    html_files = sorted(
        list(directory.glob("*.html")) + list(directory.glob("*.htm"))
    )
    if not html_files:
        logger.warning("No HTML files found in: %s", directory)
        return []

    articles: list[Article] = []
    for f in html_files:
        try:
            articles.extend(load(f))
        except Exception as exc:
            logger.error("Failed to read '%s': %s", f.name, exc)

    logger.info("Parsed %d articles from %d HTML files.", len(articles), len(html_files))
    return articles


def _extract_title(soup: BeautifulSoup, fallback_path: Path) -> str:
    """Try <title>, then first <h1>, then filename."""
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)
    return fallback_path.stem.replace("_", " ").replace("-", " ").title()


def _extract_body(soup: BeautifulSoup) -> str:
    """Extract the main content area in priority order, or fall back to full body."""
    for selector in ["article", "main", '[role="main"]', ".article-body",
                     ".content", "#content", "body"]:
        element = soup.select_one(selector)
        if element:
            return str(element)
    return str(soup)


def _extract_meta(soup: BeautifulSoup, names: list[str]) -> str:
    """Try to extract a meta tag value by name or property."""
    for name in names:
        tag = (
            soup.find("meta", attrs={"name": re.compile(f"^{re.escape(name)}$", re.I)})
            or soup.find("meta", attrs={"property": re.compile(f"^{re.escape(name)}$", re.I)})
        )
        if tag and tag.get("content"):
            return tag["content"].strip()
    return ""
