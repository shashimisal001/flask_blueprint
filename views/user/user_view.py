from flask_app import db, bcrypt
from flask import render_template, request, redirect, flash
from flask_login import login_user, logout_user, current_user
from flask_app.models.users import User
from flask_app.helpers.common_helper import authenticated_user, unauthenticated_user

class UserView():
    @unauthenticated_user
    def register(self):
        return render_template("user/register.html", data=[])
    
    @unauthenticated_user
    def create(self):
        password_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(name=request.form["name"], username=request.form['username'], email=request.form['email'], password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully', 'alert alert-success')
        return redirect('/user/register')
    
    @unauthenticated_user
    def login(self):
        user = User.query.filter_by(email=request.form["email"]).first()
        if user is not None and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            flash('Login successful', 'alert alert-success')
            return redirect("/")
        else:
            flash('Login failed', 'alert alert-danger')
            return redirect("/user/login-form")
    
    @unauthenticated_user
    def login_form(self):
        return render_template("user/login.html", data=[])

    @authenticated_user
    def logout(self):
        logout_user()
        flash('Logged out successfully', 'alert alert-success')
        return redirect("/user/login-form") 
