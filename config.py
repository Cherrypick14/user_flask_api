import os

path_file= os.path.abspath(os.getcwd()) + "/db/userprofile.db"

class Config:
    SECRET_KEY ="uYVmQf3wam"
    DEVELOPMENT=False
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI =""
    SQLALCHEMY_TRACK_MODIFICATIONS= True

class DevConfig(Config):
     DEVELOPMENT=True
     DEBUG=True
     SQLALCHEMY_DATABASE_URI =f"sqlite:///{path_file}"