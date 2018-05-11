from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SearchForm(FlaskForm):
    search = StringField("Search", [validators.Length(min=1)])

    class Meta:
        csrf = False
