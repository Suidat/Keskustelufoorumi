from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DiscussionForm(FlaskForm):
    name = StringField("Discussion name", [validators.Length(min=4)])

    class Meta:
        csrf = False
