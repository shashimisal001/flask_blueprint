import os
class Config():
    DB_SETTINGS = {
        "host": "localhost",
        "user": "root",
        "password": "cfg@1234",
        "name": "library",
        "port": 3306
    }
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(PROJECT_ROOT, 'library.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "secret"