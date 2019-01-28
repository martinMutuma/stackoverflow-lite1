import os
from app import stolite, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.config import *

stolite.config.from_object(DevelopmentConfig)

migrate = Migrate(stolite, db)
manager = Manager(stolite)
manager.add_command('db', MigrateCommand)

os.environ['FLASK_APP'] = 'common.py'
if __name__ == "__main__":
    stolite.run(debug=True)
