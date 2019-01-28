from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

stolite = Flask(__name__)

db = SQLAlchemy(stolite)

import app.routes
from app.V1.routes import mod
stolite.register_blueprint(mod, url_prefix='/api/v1')
