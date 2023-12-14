from flask import redirect
from flask_login import current_user

def authenticated_user(func):
    def check(*args, **kwargs):
        if current_user.is_authenticated:
            return func(*args, **kwargs)
        else:
            return redirect("/user/login-form")
    return check

def unauthenticated_user(func):
    def check(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect("/")
        else:
            return func(*args, **kwargs)
    return check