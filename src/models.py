"""
Shared data model for all readers (CSV, Excel, HTML).
"""

from dataclasses import dataclass, field


@dataclass
class Article:
    """Normalised representation of a single KB article from any input format."""

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
