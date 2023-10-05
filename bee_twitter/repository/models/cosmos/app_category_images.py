from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AppCategoryImages:
    id: int = None
    dt_creation: str = field(default_factory=datetime.now().isoformat)
    dt_update: str = field(default_factory=datetime.now().isoformat)
    dt_expiration: str = field(default_factory=datetime.now().isoformat)
    cod_status: int = None
    nom_file: str = None
    text_image: str = None
    id_category: str = None
    nom_category: str = None
    url_original: str = None
    url_large: str = None
    url_small: str = None
