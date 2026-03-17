"""
Converts parsed Article objects into Markdown files on disk.

Each article becomes one .md file with YAML front matter followed by the
article body converted from HTML to Markdown.
"""

import logging
import re
from datetime import date, datetime
from pathlib import Path
from typing import Optional

from markdownify import markdownify as md

from .config import OUTPUT_DIR, USE_DATED_SUBFOLDER
from .parser import Article

logger = logging.getLogger(__name__)

_UNSAFE_FILENAME_RE = re.compile(r'[\\/*?:"<>|]')
_MAX_FILENAME_LEN = 80


def _sanitize_filename(name: str) -> str:
    """Strip characters that are illegal in Windows/macOS/Linux filenames."""
    safe = _UNSAFE_FILENAME_RE.sub("", name).strip()
    safe = re.sub(r"\s+", "_", safe)
    return safe[:_MAX_FILENAME_LEN] or "untitled"


def _resolve_output_dir(base: Path) -> Path:
    """Return the target directory, optionally dated, and ensure it exists."""
    if USE_DATED_SUBFOLDER:
        target = base / date.today().isoformat()
    else:
        target = base
    target.mkdir(parents=True, exist_ok=True)
    return target


def _html_to_markdown(html: str) -> str:
    """Convert an HTML string to clean Markdown text."""
    if not html:
        return ""
    return md(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    ).strip()


def _build_front_matter(article: Article) -> str:
    """Return a YAML front matter block for the article."""
    lines = ["---"]

    def _quoted(value: str) -> str:
        return '"' + value.replace('"', '\\"') + '"'

    lines.append(f"title: {_quoted(article.title)}")

    if article.subtitle:
        lines.append(f"subtitle: {_quoted(article.subtitle)}")
    if article.kb_name:
        lines.append(f"knowledge_base: {_quoted(article.kb_name)}")
    if article.category:
        lines.append(f"category: {_quoted(article.category)}")
    if article.subcategory:
        lines.append(f"subcategory: {_quoted(article.subcategory)}")
    if article.language:
        lines.append(f"language: {_quoted(article.language)}")
    if article.keywords:
        lines.append(f"keywords: {_quoted(article.keywords)}")
    if article.status:
        lines.append(f"status: {_quoted(article.status)}")
    if article.archived:
        lines.append(f"archived: {_quoted(article.archived)}")
    if article.modified_date:
        lines.append(f"last_modified: {_quoted(article.modified_date)}")
    if article.url:
        lines.append(f"source_url: {_quoted(article.url)}")

    lines.append(f"exported_at: \"{datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}\"")
    lines.append("---")
    return "\n".join(lines)


def _unique_path(directory: Path, stem: str, suffix: str = ".md") -> Path:
    """Return a path that does not conflict with existing files by appending a counter."""
    candidate = directory / f"{stem}{suffix}"
    if not candidate.exists():
        return candidate
    counter = 1
    while True:
        candidate = directory / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def convert_article(article: Article, output_dir: Optional[Path] = None) -> Path:
    """
    Convert a single Article to a Markdown file.

    Args:
        article: The parsed Article object.
        output_dir: Override for the output directory (defaults to config.OUTPUT_DIR).

    Returns:
        The Path of the written Markdown file.
    """
    base = output_dir or OUTPUT_DIR
    target_dir = _resolve_output_dir(base)

    front_matter = _build_front_matter(article)
    markdown_body = _html_to_markdown(article.body_html)

    content = f"{front_matter}\n\n# {article.title}\n\n{markdown_body}\n"

    stem = _sanitize_filename(article.title)
    out_path = _unique_path(target_dir, stem)

    out_path.write_text(content, encoding="utf-8")
    return out_path


def convert_all(articles: list[Article], output_dir: Optional[Path] = None) -> list[Path]:
    """
    Convert every article in the list and return paths of written files.

    Args:
        articles: List of Article objects from the parser.
        output_dir: Override for the output directory.

    Returns:
        List of Paths for all successfully written Markdown files.
    """
    written: list[Path] = []
    failed = 0

    for article in articles:
        try:
            path = convert_article(article, output_dir)
            logger.info("  [OK]  %s", path.name)
            written.append(path)
        except Exception as exc:
            logger.error("  [FAIL]  '%s': %s", article.title, exc)
            failed += 1

    logger.info(
        "Conversion complete: %d written, %d failed.", len(written), failed
    )
    return written
