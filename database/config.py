from pydantic.v1 import BaseSettings


class DatabaseConfig(BaseSettings):
    login: str = "postgres"
    password: str = "password"
    host: str = "localhost"
    port: str = "5432"
    database: str = "postgres"

    @property
    def postgresql_url(self) -> str:
        return f"postgresql+asyncpg://{self.login}:{self.password}@{self.host}:{self.port}/{self.database}"


service_database_settings = DatabaseConfig()
