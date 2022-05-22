import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


""" Will use this if I figure stuff out

class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] 

class DevelopmentConfig(Config):
    FLASK_ENV='development'
    DEBUG=True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'test.db')
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' #in memory database
"""