from flask_wtf import FlaskForm
from wtforms import StringField, validators

class GroupForm(FlaskForm):
    name = StringField("Group name", [validators.Length(min=4)])

    class Meta:
        csrf = False
