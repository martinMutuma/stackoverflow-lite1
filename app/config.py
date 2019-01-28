import os


class Config:
    os.environ['DB_CONNNECTION_STRING'] = 'postgresql://postgres:admin@localhost:5432/stackoverflow1'
    DEBUG = False
    FLASK_DEBUG = 0
    SECRET_KEY = "any secret string"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONNNECTION_STRING')


class DevelopmentConfig(Config):
    os.environ['DB_CONNNECTION_STRING'] = 'postgresql://postgres:admin@localhost:5432/stackoverflow1'
    FLASK_DEBUG = 1
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONNNECTION_STRING')


class TestConfig(Config):
    os.environ['DB_CONNNECTION_STRING'] = 'postgresql://postgres:admin@localhost:5432/stackoverflow1_test'
    FLASK_DEBUG = 1
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONNNECTION_STRING')


class CIConfig(Config):
    os.environ['DB_CONNNECTION_STRING'] = 'postgresql://postgres:@localhost/stackoverflow1'
    FLASK_DEBUG = 0
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONNNECTION_STRING')
