from flask import render_template
from flask_app.helpers.common_helper import authenticated_user, unauthenticated_user


class Home():
    def index(self):
        return render_template('index.html', data=[])