from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config.settings import DATABASE_URL

# Declarando bases e tabelas
Base = declarative_base()

# Criando engine com o banco de conexão
engine = create_engine(DATABASE_URL, echo=False)

# criação da sessão
Session = sessionmaker()


class Connector:
    def __init__(self):
        self.session = Session(bind=engine)

    def __enter__(self):
        return self.session

    def __exit__(self, *args, **kwargs):
        self.session.commit()
        self.session.close()
