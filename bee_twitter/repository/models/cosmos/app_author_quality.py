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
    quality_result: str = None
    quality_value: float = None
    quality_results: list[dict] = None
