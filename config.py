"""Flask Configuration"""
import os

path_file= os.path.abspath(os.getcwd()) + "/db/userprofile.db"

class Config:
    SECRET_KEY ="uYVmQf3wam"
    DEVELOPMENT=False
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI ="sqlite:///userprofile.db"
    SQLALCHEMY_TRACK_MODIFICATIONS= True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///userprofile.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
     DEVELOPMENT=True
     DEBUG=True
     SQLALCHEMY_DATABASE_URI =f"sqlite:///{path_file}"
class TestingConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_userprofile.db'