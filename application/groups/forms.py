from flask_wtf import FlaskForm
from wtforms import StringField

class GroupForm(FlaskForm):
    name = StringField("Group name")

    class Meta:
        csrf = False
