from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask import current_app as app
from flask_login import login_required, current_user, login_user, logout_user
from passlib.hash import pbkdf2_sha256

from ..reddit import Reddit
from ..models import Users
from ..forms import RegistrationForm

user = Blueprint('user', __name__)

@user.route('/')
def index():
    reddit = Reddit(app.config)
    reddit_oauth_url = reddit.getOauthURL()
    return render_template("index.html", reddit_oauth_url=reddit_oauth_url)

@user.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #Todo: not use wtf form for validation
        form = RegistrationForm(request.form)
        if not form.validate():
            flash("Form validation fails")
            return render_template('register.html')
        passwordHash = pbkdf2_sha256.hash(form.password.data)
        user = Users(form.email.data, passwordHash, form.post_limit.data)
        user.save()
        login_user(user)
        flash('Im a flash: Thanks for registering')
        return redirect(url_for('user.index'))

    return render_template('register.html')
    
@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Users.objects(email=request.form["email"]).first()
        if user is not None: 
            if pbkdf2_sha256.verify(request.form["password"], user.password_hash):
                login_user(user)
                return redirect(url_for('user.index'))
        flash("Incorrect Login Credientials")
    return render_template('login.html')

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.index'))
        
@user.route('/reddit_auth')
@login_required
def reddit_auth():
    reddit_code = request.args["code"]
    #TODO: verify state 
    reddit = Reddit(app.config)
    refresh_token = reddit.getRefreshToken(reddit_code)
    current_user.reddit_refresh_token = refresh_token
    current_user.save()
    return redirect(url_for('user.index'))
    