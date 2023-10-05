from datetime import datetime

from azure.cosmos import CosmosClient, PartitionKey, exceptions
from loguru import logger

from bee_twitter.config.settings import URL, KEY


class CosmosDBManager:
    def __init__(self, container_name, database_id="app_site"):
        self.client = CosmosClient(URL, credential=KEY)
        self.database_id = database_id
        self.container_name = container_name

        try:
            self.database = self.client.create_database_if_not_exists(id=database_id)
            self.container = self.database.create_container_if_not_exists(
                id=container_name, partition_key=PartitionKey(path=f"/{container_name}")
            )
        except Exception as e:
            logger.error(f"Erro ao inicializar o Cosmos DB: {str(e)}")

    @staticmethod
    def serialize_datetime(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Tipo de objeto não serializável: {type(obj)}")

    def add_object(self, obj):
        try:
            self.container.create_item(obj.__dict__)

        except exceptions.CosmosResourceExistsError:
            logger.warning(f"Item já existe no Cosmos DB: {obj}")
            pass

        except Exception as e:
            logger.error(f"Erro ao adicionar item ao Cosmos DB: {str(e)}")
            raise
