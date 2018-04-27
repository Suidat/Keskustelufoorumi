from application import app, db, login_required
from flask import render_template, request
from application.discussions.models import Discussion

@app.route("/groups/own")
def groups_mine():
    return render_template("discussions/own.html")

@app.route("/groups/<int:param>")
def group_home(param):
    group = Discussion.query.filter_by(group_id = param)
    if not group:
        return render_template("discussions/index.html", error = "That group does not exist")

    return render_template("discussions/index.html", discussions = group)

@app.route("/groups/new")
def groups_new():
    return "hi"
