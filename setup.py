from setuptools import setup, find_packages

setup(
    name="fastapi_boilerplate",
    version="0.1",
    description="FastAPI Boilerplate",
    author="Kimseng Duong",
    author_email="duong.kim.seng@gamil.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["fastrun=src.cli.main:main"],
    },
    install_requires=["fastapi", "uvicorn", "alembic", "SQLAlchemy"],
)
