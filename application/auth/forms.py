from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

class AccountForm(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")

    class Meta:
        csrf = False

class LoginForm(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")

    class Meta:
        csrf = False
