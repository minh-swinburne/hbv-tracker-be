from pydantic_settings import BaseSettings
from dotenv import load_dotenv


# Load .env at startup
load_dotenv(override=True)


class Settings(BaseSettings):
    frontend_origins: str = "http://localhost:3000,http://localhost:8000"
    
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"


settings = Settings()
