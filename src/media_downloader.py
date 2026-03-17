"""
Downloads media files (images, videos, audio, documents) referenced inside
article HTML, saves them locally, and rewrites the HTML src/href attributes
to point to the local copies.

Saved to: OUTPUT_DIR/media_files/
Referenced in Markdown as: <relative_path_to_media_files>/filename
"""

import hashlib
import logging
import mimetypes
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

# Tags and their URL-bearing attributes to process
_MEDIA_ATTRS: dict[str, str] = {
    "img": "src",
    "video": "src",
    "audio": "src",
    "source": "src",
}

# Anchor hrefs pointing to these file types will also be downloaded
_DOWNLOADABLE_EXTENSIONS = {
    ".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt",
    ".zip", ".csv", ".txt", ".xml", ".json",
}

_REQUEST_TIMEOUT = 15  # seconds
_REQUEST_HEADERS = {"User-Agent": "HubSpot-KB-Converter/1.0"}


def process(html: str, media_dir: Path, article_dir: Path) -> str:
    """
    Parse HTML, download all referenced media to media_dir, and return
    updated HTML with local relative paths.

    Args:
        html: Raw HTML string of the article body.
        media_dir: Absolute path where downloaded files are saved.
        article_dir: Absolute path where the .md file will be written
                     (used to compute the relative path back to media_dir).

    Returns:
        Updated HTML string with src/href replaced by local relative paths.
    """
    if not html:
        return html

    soup = BeautifulSoup(html, "html.parser")
    media_dir.mkdir(parents=True, exist_ok=True)

    # Compute the relative path from the article file to the media folder
    try:
        parts_up = len(article_dir.relative_to(media_dir.parent).parts)
        rel_media = Path("../" * parts_up + "media_files")
    except ValueError:
        rel_media = Path("media_files")

    downloaded: dict[str, str] = {}  # original_url -> local_relative_path

    # Process img / video / audio / source tags
    for tag_name, attr in _MEDIA_ATTRS.items():
        for tag in soup.find_all(tag_name, **{attr: True}):
            original = tag[attr].strip()
            local = _download_and_localise(original, media_dir, rel_media, downloaded)
            if local:
                tag[attr] = local

    # Process <a href="..."> for downloadable file types
    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        parsed = urlparse(href)
        ext = Path(parsed.path).suffix.lower()
        if ext in _DOWNLOADABLE_EXTENSIONS:
            local = _download_and_localise(href, media_dir, rel_media, downloaded)
            if local:
                tag["href"] = local

    if downloaded:
        logger.info("  Downloaded %d media file(s).", len(downloaded))

    return str(soup)


def _download_and_localise(
    url: str,
    media_dir: Path,
    rel_media: Path,
    cache: dict[str, str],
) -> str:
    """Download a single URL, save it, and return the local relative path."""
    if not url or url.startswith("data:"):
        return ""

    # Normalise protocol-relative URLs
    if url.startswith("//"):
        url = "https:" + url

    # Skip relative paths (no host) — can't resolve without a base URL
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return ""

    if url in cache:
        return cache[url]

    try:
        filename = _safe_filename(url)
        dest = _unique_dest(media_dir, filename)

        response = requests.get(
            url, timeout=_REQUEST_TIMEOUT, headers=_REQUEST_HEADERS, stream=True
        )
        response.raise_for_status()

        # Use Content-Type to add extension if missing
        if "." not in dest.suffix:
            ctype = response.headers.get("Content-Type", "").split(";")[0].strip()
            ext = mimetypes.guess_extension(ctype) or ""
            dest = dest.with_suffix(ext)

        dest.write_bytes(response.content)
        local_path = str(rel_media / dest.name).replace("\\", "/")
        cache[url] = local_path
        logger.debug("  Saved: %s -> %s", url, dest.name)
        return local_path

    except requests.RequestException as exc:
        logger.warning("  Could not download '%s': %s", url, exc)
        return ""


def _safe_filename(url: str) -> str:
    """Derive a safe local filename from a URL."""
    parsed = urlparse(url)
    name = Path(parsed.path).name
    # Strip query strings / fragments that might have snuck into the name
    name = re.sub(r"[?#&=].*", "", name)
    name = re.sub(r"[^\w.\-]", "_", name)
    if not name or name == "_":
        # Fall back to a short hash of the URL
        name = hashlib.md5(url.encode()).hexdigest()[:12]
    return name[:100]


def _unique_dest(directory: Path, filename: str) -> Path:
    """Return a path that doesn't conflict with existing files."""
    candidate = directory / filename
    if not candidate.exists():
        return candidate
    stem, suffix = Path(filename).stem, Path(filename).suffix
    counter = 1
    while True:
        candidate = directory / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1
