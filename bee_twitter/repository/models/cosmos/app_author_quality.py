from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AppAuthorQuality:
    id: str = None
    dt_creation: str = field(default_factory=datetime.now().isoformat)
    dt_update: str = field(default_factory=datetime.now().isoformat)
    dt_expiration: str = None
    cod_status: int = None
    id_publisher: int = None
    id_author: int = None
    name: str = None
    twitter_profile: str = None
    author_description: str = None
    dt_last_mention: str = field(default_factory=datetime.now().isoformat)
    img_small_url: str = None
    img_original_url: str = None
    num_vote: int = None
    quality_result: str = None
    quality_value: float = None
    quality_description: str = None
    quality_results: list[dict] = None  # AppQuality: order: str, name: str, quality_value: float
