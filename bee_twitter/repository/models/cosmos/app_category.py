from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AppCategory:
    id: int = None
    dt_creation: str = field(default_factory=datetime.now().isoformat)
    dt_update: str = field(default_factory=datetime.now().isoformat)
    dt_expiration: str = field(default_factory=datetime.now().isoformat)
    cod_status: int = None
    hashtag: str = None
    order: int = None
    name: str = None
    description: str = None
    img_small_url: str = None
    img_original_url: str = None
