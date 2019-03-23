from mongoengine import DateTimeField, Document, DynamicField, EmailField, IntField, ListField, ReferenceField, StringField, URLField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

def redditToPost(post):
    return {
        'title': post.title, 
        'text': post.selftext, 
        'url': post.url,
        'type': "reddit" #TODO: make subreddit
    }

def hnToPost(post):
    print(post)
    return {
        'title': post['title'],
        'text': post.get('text', ''),
        'url': post['url'],
        'type': "hackernews"
    }

class Posts(Document):
    title = StringField()
    link = URLField()
    text = StringField() 
    type = StringField() #'text' => text main content, 'link' => url main content
    score = IntField()
    src = StringField() #subreddit/hackernews string
    src_id = IntField()
    src_data = DynamicField() #extra json with specific info for debug 
    creation_utc = IntField()
    last_updated_utc = IntField() #last time field was updated

class Users(UserMixin, Document):
    email = EmailField(required=True)
    password_hash = StringField(required=True)
    post_limit = IntField(required=True)
    reddit_refresh_token = StringField()
    last_logged_in = DateTimeField()
    last_posts = ListField(ReferenceField(Posts))
    recommendation_data = DynamicField()

    @property
    def password(self):
        raise AttributeError("password unreadable")

    #can just set with user.password = password and it will be auto hashed
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(uid):
        return Users.objects(id=uid).first()

