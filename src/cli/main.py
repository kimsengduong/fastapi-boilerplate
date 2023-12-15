import importlib
import pkgutil

import click
from alembic.config import main as alembic_main
from uvicorn import run

from src import cli
from src.config import APP_HOST, APP_PORT


@click.group()
def fastrun():
    pass


# add sub-commands
for load, module_name, is_pkg in pkgutil.walk_packages(
    cli.__path__, cli.__name__ + "."
):
    module = importlib.import_module(module_name)
    p, m = module_name.rsplit(".", 1)

    if m == "main":
        continue

    for attribute in module.__dict__.values():
        if isinstance(attribute, (click.core.Command, click.core.Group)):
            fastrun.add_command(attribute)

            if isinstance(attribute, click.core.Group):
                break


@fastrun.command()
def start():
    """Start the server."""
    run("src.app:app", host=APP_HOST, port=APP_PORT, reload=True)
