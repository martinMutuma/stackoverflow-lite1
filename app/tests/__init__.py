from app import stolite, db
from app.config import TestConfig
from unittest import TestCase
from sqlalchemy_utils import database_exists, create_database


def db_setUp():
    stolite.config.from_object(TestConfig)
    db_url = stolite.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(db_url):
        create_database(db_url)

    db.create_all()
    # Rem  create a seeding function


def db_teardown():
    db.session.remove()
    db.drop_all()
