from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask import current_app as app
from flask_login import login_required, current_user

from ..reddit import Reddit
from ..hackernews import HackerNews
from ..models import Users

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('user.index'))

@main.route('/front')
@login_required
def front():
    if current_user.reddit_refresh_token is None:
        flash("Please set your refresh_token")
        return redirect(url_for('user.index'))
        
    reddit = Reddit(app.config, current_user.reddit_refresh_token)
    hn = HackerNews()
    reddit_limit = (current_user.post_limit // 2)
    hn_limit = current_user.post_limit - reddit_limit
    front = hn.getTopStories(hn_limit)
    front.extend(reddit.getFront(reddit_limit)) #if url, selftext will be ""
    return render_template("front.html", posts=front)
    
# @main.route('/yc')
# def yc():
    