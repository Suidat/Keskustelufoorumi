from flask_wtf import FlaskForm
from wtforms import StringField

class TaskForm(FlaskForm):
    name = StringField("Message")
 
    class Meta:
        csrf = False

