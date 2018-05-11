from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class AccountForm(FlaskForm):
    username = StringField("username", [validators.Length(min=3)])
    password = PasswordField("password", [validators.Length(min=3)])

    class Meta:
        csrf = False

class LoginForm(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")

    class Meta:
        csrf = False
class EditForm(FlaskForm):
    password_old = PasswordField("Old Password")
    password_new1 = PasswordField("New Password", [validators.Length(min=3)])
    password_new2 = PasswordField("Retype new password", [validators.Length(min=3)])
