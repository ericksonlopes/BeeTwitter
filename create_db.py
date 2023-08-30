from src.repository.connect import Base, engine

from src.repository.models import *

Base.metadata.create_all(engine)
