from flask import render_template,redirect,request,flash,url_for
from flask_login import login_user,logout_user,current_user
from app.auth.forms import LoginForm, RegisterForm
from app.models import User
from app.auth import bp
from app import db

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('You are loged in. ')   
            return redirect('/chat')     

    return render_template('auth/login.html',form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        user = User(username=username,email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('You are registered')
        return redirect('/auth/login')
        
    return render_template('auth/register.html',form=form)


@bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    # Ensure this matches your login endpoint. If your login page is at /login, this is correct.
    return redirect('/auth/login')
