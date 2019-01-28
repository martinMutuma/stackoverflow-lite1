import os


class Config:
    os.environ['DB_CONNNECTION_STRING'] = 'postgresql://postgres:admin@localhost:5432/sto1'
    DEBUG = False
    FLASK_DEBUG=0
    SECRET_KEY = "any secret string"
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONNNECTION_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    os.environ['DB_CONNNECTION_STRING'] = 'postgresql://postgres:admin@localhost:5432/sto1'
    FLASK_DEBUG=1
    DEBUG = True


class TestConfig(Config):
    # os.environ['DB_CONNNECTION_STRING'] = 'postgresql://postgres:@localhost/sto1'
    os.environ['DB_CONNNECTION_STRING'] = 'postgresql://postgres:admin@localhost:5432/sto1'
    FLASK_DEBUG=0
    DEBUG = True

