from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_app.config import Config
import sys, os

app = Flask(__name__, static_folder="static", template_folder="templates", instance_path=Config.PROJECT_ROOT)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flask_app.views.home import home_routes
from flask_app.views.user import user_routes

app.register_blueprint(home_routes, url_prefix="/")
app.register_blueprint(user_routes, url_prefix="/user") 

if __name__ == '__main__':
    app.run(debug=True)