from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AppHashtags:
    id: int = None
    dt_creation: str = field(default_factory=datetime.now().isoformat)
    dt_update: str = field(default_factory=datetime.now().isoformat)
    dt_expiration: str = field(default_factory=datetime.now().isoformat)
    cod_status: int = None
    hashtag: str = None
    name: str = None
    description: str = None
    qtd_news: int = None
    qtd_posts: int = None
    dt_last_mention: str = field(default_factory=datetime.now().isoformat)
