from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # mudar arquivo de variáveis de ambiente para raiz do projeto
        env_file=".env",
        env_file_encoding="utf-8",
    )

    """"Environment Variables"""

    DATABASE_URL: str
