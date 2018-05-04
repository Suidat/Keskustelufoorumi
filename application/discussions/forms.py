from flask_wtf import FlaskForm
from wtforms import StringField

class DiscussionForm(FlaskForm):
    name = StringField("Discussion name")

    class Meta:
        csrf = False
