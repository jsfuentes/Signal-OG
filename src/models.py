from mongoengine import DateTimeField, Document, EmailField, IntField, ListField, ReferenceField, StringField, URLField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class Posts(Document):
    url = URLField(required=True)
    type = StringField()
    src = StringField()

class Users(UserMixin, Document):
    email = EmailField(required=True)
    password_hash = StringField(required=True)
    reddit_refresh_token = StringField()
    post_limit = IntField()
    last_logged_in = DateTimeField()
    last_posts = ListField(ReferenceField(Posts))

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

