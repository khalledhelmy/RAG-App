from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNCK_SIZE: int

    MONGODB_URL: str
    MONGODB_DATABASE: str

    GENERATION_BACKEND: str
    EMBEDDING_BACKEND: str

    GEMINI_API_KEY: str = None
    GEMINI_API_BASE_URL: str = None

    GENERATION_MODEL_ID: str = None
    EMBEDDING_MODEL_ID: str = None
    EMBEDDING_MODEL_SIZE: int = None
    INPUT_DEFAULT_MAX_CHARACTERS: int = None
    GENERATION_DEFAULT_MAX_TOKENS: int = None
    GENERATION_DEFAULT_TEMPERATURE: float = None

    VECTOR_DB_BACKEND: str = None
    VECTOR_DB_PATH: str = None
    VECTOR_DB_DISTANCE_METHOD: str = None

    PRIMARY_LANG: str = "en"
    DEFAULT_LANG: str =  "en"

    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings() 

