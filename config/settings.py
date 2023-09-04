import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# Twitter API
bearer_token = config.get("TwitterAPI", "bearer_token")
consumer_key = config.get("TwitterAPI", "consumer_key")
consumer_secret = config.get("TwitterAPI", "consumer_secret")
access_token = config.get("TwitterAPI", "access_token")
access_token_secret = config.get("TwitterAPI", "access_token_secret")

# OpenAI
API_KEY_OPENAI = config.get("Openai", "KEY")

# Snowflake
USER = config.get("Snowflake", "USER")
PASSWORD = config.get("Snowflake", "PASSWORD")
ACCOUNT = config.get("Snowflake", "ACCOUNT")
DATABASE = config.get("Snowflake", "DATABASE")
SCHEMA = config.get("Snowflake", "SCHEMA")

DATABASE_URL = f'snowflake://{USER}:{PASSWORD}@{ACCOUNT}/{DATABASE}/{SCHEMA}'
