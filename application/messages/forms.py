from flask_wtf import FlaskForm
from wtforms import StringField

class MessageForm(FlaskForm):
    name = StringField("message")


    class Meta:
        csrf = False
