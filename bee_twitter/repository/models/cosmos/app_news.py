from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AppNews:
    id: int = None
    dt_creation: str = field(default_factory=datetime.now().isoformat)
    dt_update: str = field(default_factory=datetime.now().isoformat)
    dt_expiration: str = field(default_factory=datetime.now().isoformat)
    cod_status: int = None
    post_type: str = None
    friendly_url: str = None
    title: str = None
    resume: str = None
    content_demo: str = None
    content: str = None
    text_ai_analysis: str = None
    img_small_url: str = None
    img_original_url: str = None
    publisher: str = None
    category: list[dict] = None  # AppCategory: id_category: str, name_category: str
    author: list[dict] = None  # AppAuthor: name_author: str, twitter_profile: str
    hashtags: str = None
    num_vote: int = None
