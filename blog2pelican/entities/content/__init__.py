from dataclasses import dataclass
from typing import List


@dataclass
class Content:
    title: str
    content: str
    slug: str
    date: str
    author: str
    categories: List[str]
    tags: List[str]
    status: str
    kind: str
    post_format: str
