from . import auth
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import LoginForm,RegistrationForm
from ..email import mail_message
from app.models import User, Pitch, Comment
from .. import db


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to Pitch perfect","email/welcome_user",user.email,user=user)

        title = "New Account"
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form = form, title = title)

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')
    form = LoginForm()
    title = "pitch perfect login"
    pitchs = Pitch.query.all()
    return render_template('auth/login.html', login_form = form, title=title, pitchs = pitchs)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Thanks for visiting this app. see you around!!')
    return redirect(url_for("main.index"))
