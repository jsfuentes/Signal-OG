from wtforms import Form, BooleanField, IntegerField, StringField, PasswordField, validators

class RegistrationForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    post_limit = IntegerField("Posts to Display")