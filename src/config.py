APP_HOST = "localhost"
APP_PORT = 8000

APP_NAME = "FastAPI Boilerplate"
APP_VERSION = "0.0.1"
APP_CONTACT = {
    "name": "Kimseng Duong",
    "email": "duong.kim.seng@gmail.com",
}

POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_SERVER = "localhost"
POSTGRES_DB = "fastapi-boilerplate"
PORT = 5432

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{PORT}/{POSTGRES_DB}"

# openssl rand -hex 16
SECRET_KEY = "b7ca5324fd327fe2b90a806f60e36509"
JWT_ALGORITHM = "HS256"
JWT_EXP_TIME_MINUTES = 60  ## 1 hour
JWT_REFRESH_EXP_TIME_MINUTES = 7 * 24 * 60  ## (7 days * 24 hours * 60 minutes)
