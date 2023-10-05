from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AppPublisher:
    id: int = None
    dt_creation: str = field(default_factory=datetime.now().isoformat)
    dt_update: str = field(default_factory=datetime.now().isoformat)
    dt_expiration: str = field(default_factory=datetime.now().isoformat)
    cod_status: int = None
    hashtag: str = None
    name: str = None
    site_url: str = None
    publisher_icon: str = None
    publisher_icon_small: str = None
    twitter_profile: str = None
    dt_last_mention: str = field(default_factory=datetime.now().isoformat)
