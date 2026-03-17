"""
Converts Article objects into Markdown files on disk.
Optionally downloads all referenced media files to a local media_files/ folder.
"""

import logging
import re
from datetime import date, datetime
from pathlib import Path
from typing import Optional

from markdownify import markdownify as md

from . import config
from .models import Article

logger = logging.getLogger(__name__)

_UNSAFE_FILENAME_RE = re.compile(r'[\\/*?:"<>|]')
_MAX_FILENAME_LEN = 80


def _sanitize_filename(name: str) -> str:
    safe = _UNSAFE_FILENAME_RE.sub("", name).strip()
    safe = re.sub(r"\s+", "_", safe)
    return safe[:_MAX_FILENAME_LEN] or "untitled"


def _resolve_output_dir(base: Path) -> Path:
    target = base / date.today().isoformat() if config.USE_DATED_SUBFOLDER else base
    target.mkdir(parents=True, exist_ok=True)
    return target


def _html_to_markdown(html: str) -> str:
    if not html:
        return ""
    return md(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    ).strip()


def _build_front_matter(article: Article) -> str:
    lines = ["---"]

    def q(value: str) -> str:
        return '"' + value.replace('"', '\\"') + '"'

    lines.append(f"title: {q(article.title)}")
    if article.subtitle:
        lines.append(f"subtitle: {q(article.subtitle)}")
    if article.kb_name:
        lines.append(f"knowledge_base: {q(article.kb_name)}")
    if article.category:
        lines.append(f"category: {q(article.category)}")
    if article.subcategory:
        lines.append(f"subcategory: {q(article.subcategory)}")
    if article.language:
        lines.append(f"language: {q(article.language)}")
    if article.keywords:
        lines.append(f"keywords: {q(article.keywords)}")
    if article.status:
        lines.append(f"status: {q(article.status)}")
    if article.archived:
        lines.append(f"archived: {q(article.archived)}")
    if article.modified_date:
        lines.append(f"last_modified: {q(article.modified_date)}")
    if article.url:
        lines.append(f"source_url: {q(article.url)}")
    lines.append(f"exported_at: \"{datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}\"")
    lines.append("---")
    return "\n".join(lines)


def _unique_path(directory: Path, stem: str, suffix: str = ".md") -> Path:
    candidate = directory / f"{stem}{suffix}"
    if not candidate.exists():
        return candidate
    counter = 1
    while True:
        candidate = directory / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def convert_article(
    article: Article,
    output_dir: Optional[Path] = None,
    media_dir: Optional[Path] = None,
) -> Path:
    """
    Convert a single Article to a Markdown file, downloading any media references.

    Args:
        article: The parsed Article object.
        output_dir: Override for the output directory.
        media_dir: Override for the media download directory.

    Returns:
        The Path of the written Markdown file.
    """
    base = output_dir or config.OUTPUT_DIR
    m_dir = media_dir or config.MEDIA_DIR
    target_dir = _resolve_output_dir(base)

    html_body = article.body_html

    # Download media files and rewrite HTML src/href to local paths
    if config.DOWNLOAD_MEDIA and html_body:
        from . import media_downloader
        try:
            html_body = media_downloader.process(html_body, m_dir, target_dir)
        except Exception as exc:
            logger.warning("Media download skipped for '%s': %s", article.title, exc)

    front_matter = _build_front_matter(article)
    markdown_body = _html_to_markdown(html_body)
    content = f"{front_matter}\n\n# {article.title}\n\n{markdown_body}\n"

    stem = _sanitize_filename(article.title)
    out_path = _unique_path(target_dir, stem)
    out_path.write_text(content, encoding="utf-8")
    return out_path


def convert_all(
    articles: list[Article],
    output_dir: Optional[Path] = None,
    media_dir: Optional[Path] = None,
) -> list[Path]:
    """Convert every article and return paths of successfully written files."""
    written: list[Path] = []
    failed = 0

    for article in articles:
        try:
            path = convert_article(article, output_dir, media_dir)
            logger.info("  [OK]  %s", path.name)
            written.append(path)
        except Exception as exc:
            logger.error("  [FAIL]  '%s': %s", article.title, exc)
            failed += 1

    logger.info("Conversion complete: %d written, %d failed.", len(written), failed)
    return written
