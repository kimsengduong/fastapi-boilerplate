import click
from alembic.config import main as alembic_main


@click.group()
def db():
    """Perform database migrations."""
    pass


@db.command(name="upgrade")
def upgrade():
    """Migrate the database."""
    alembic_main(argv=["upgrade", "head"])


@db.command()
@click.argument("revision", required=True)
def downgrade(revision):
    """Downgrade the database to a previous revision."""
    alembic_main(argv=["downgrade", revision])


@db.command()
@click.option("--message", "-m", required=True)
def revision(message):
    """Create a new revision."""
    alembic_main(argv=["revision", "--autogenerate", "-m", message])


if __name__ == "__main__":
    db()
