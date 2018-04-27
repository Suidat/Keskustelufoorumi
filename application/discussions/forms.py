from flask_wtf import FlaskForm
from wtforms import StringField

class DiscussionForm(FlaskForm):
    name = StringField("discussion name")

    class Meta:
        csrf = False
