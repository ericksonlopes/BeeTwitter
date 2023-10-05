from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from bee_twitter.config.settings import DATABASE_URL_SF

# Declarando bases e tabelas
Base = declarative_base()

# Criando engine com o banco de conexão
engine = create_engine(DATABASE_URL_SF, echo=False)

# criação da sessão
Session = sessionmaker()


class ConnectorSnowflake:
    def __init__(self):
        self.session = Session(bind=engine)

    def __enter__(self):
        return self.session

    def __exit__(self, *args, **kwargs):
        self.session.commit()
        self.session.close()
