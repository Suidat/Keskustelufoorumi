from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class MessageForm(FlaskForm):
    message = TextAreaField("message", [validators.Length(min=2)])

    class Meta:
        csrf = False
