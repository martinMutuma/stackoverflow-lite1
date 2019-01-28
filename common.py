import os
from app import stolite, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy_utils import database_exists, create_database
from app.config import *


stolite.config.from_object(DevelopmentConfig)

migrate = Migrate(stolite, db)
manager = Manager(stolite)
manager.add_command('db', MigrateCommand)

os.environ['FLASK_APP'] = 'common.py'

if os.environ.get('TRAVIS_CI_RUN') == 'True':
    stolite.config.from_object(CIConfig)

db_url = stolite.config['SQLALCHEMY_DATABASE_URI']

if not database_exists(db_url):
    create_database(db_url)
    db.create_all()
  

if __name__ == "__main__":
    stolite.run(debug=True)
