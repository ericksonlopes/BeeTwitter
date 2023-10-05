from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AppPostType:
    id: int = None
    dt_creation: str = field(default_factory=datetime.now().isoformat)
    dt_update: str = field(default_factory=datetime.now().isoformat)
    dt_expiration: str = field(default_factory=datetime.now().isoformat)
    cod_status: int = None
    name: str = None
    description: str = None
