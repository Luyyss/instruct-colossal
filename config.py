import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '632g32Edf_1g32@132PgsdCf3Ag2=1gh'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # postgres://jjsnpzvghssord:989264f977fd75081cfd4f7d619f531f5c20120a71ad28b513baffe40172326a@ec2-3-208-50-226.compute-1.amazonaws.com:5432/dcbcf4l61o8l2n
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:root@127.0.0.1:5432/colossal'

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

