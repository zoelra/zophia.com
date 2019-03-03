import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    USERNAME = 'fe7d80792aba17b08e301d3910bdef10e755086b2d03fa3ab99064a7ceff03cf'
    PASSWORD = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
    SECRET_KEY = """b'|\xa9={5YR\x02{\x00\x97\xda\x16\x11L\x05\xbe\x1b\xde\xe9M\xbe\x8c\x89'"""



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
