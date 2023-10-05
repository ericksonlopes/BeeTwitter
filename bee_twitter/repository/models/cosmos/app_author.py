from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AppAuthor:
    id: int = None
    dt_creation: str = field(default_factory=datetime.now().isoformat)
    dt_update: str = field(default_factory=datetime.now().isoformat)
    dt_expiration: str = field(default_factory=datetime.now().isoformat)
    cod_status: int = None
    id_publisher: int = None
    hashtag: str = None
    name: str = None
    author_description: str = None
    twitter_profile: str = None
    dt_last_mention: str = field(default_factory=datetime.now().isoformat)
    img_small_url: str = None
    img_original_url: str = None
    num_vote: int = None
