from flask import render_template,redirect,request,flash,url_for
from flask_login import login_user,logout_user,current_user
from app.auth.forms import LoginForm, RegisterForm

from app.auth import bp

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('auth/login.html',form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    return render_template('auth/register.html',form=form)


@bp.route('/logout')
def logout():
    pass
