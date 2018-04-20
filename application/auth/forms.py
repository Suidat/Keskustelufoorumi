from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

class AccountForm(FlaskForm):
    name = StringField("User name")
    password = StringField("Password")

    class Meta:
        csrf = False

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False
