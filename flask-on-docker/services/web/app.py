from project import app
from project.models import db
from flask.cli import FlaskGroup

cli = FlaskGroup(app)
cli()
@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    print("1- estou ca")
    from project.models.user import User
    print("2- estou ca")
    db.session.add(User(email="joao@test.pt"))
    print("3- estou ca")
    db.session.commit()
    print("4- estou ca")
