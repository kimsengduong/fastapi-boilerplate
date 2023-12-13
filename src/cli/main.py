import click
from alembic.config import main as alembic_main
from uvicorn import run


@click.group()
def main():
    return


@main.command()
def start():
    """Start the server."""
    run("src.app:app", host="0.0.0.0", port=8000, reload=True)


@main.command(name="upgrade")
def upgrade():
    """Migrate the database."""
    alembic_main(argv=["upgrade", "head"])


@main.command()
@click.argument("revision", required=True)
def downgrade(revision):
    """Downgrade the database."""
    alembic_main(argv=["downgrade", revision])


@main.command()
@click.option("--message", required=True)
def revision(message):
    """Create a new revision."""
    alembic_main(argv=["revision", "--autogenerate", "-m", message])


if __name__ == "__main__":
    main()
