from flask import render_template
from application import app
from application.groups.models import Groups

@app.route("/")
def index():
    groups = Groups.find_usernames_for_group_owners()

    return render_template("index.html", groups = groups)
