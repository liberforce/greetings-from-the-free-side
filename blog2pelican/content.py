from typing import List
from dataclasses import dataclass
from datetime import datetime

from blog2pelican import ProcessingStatus


@dataclass
class Content:
    title: str
    content: str
    filename: str
    date: datetime
    author: str
    categories: List[str]
    tags: List[str]
    status: str
    kind: str
    in_markup: str
    slug: str = None
    processing_status: ProcessingStatus = ProcessingStatus.UNDEFINED
