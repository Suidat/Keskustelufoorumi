from application import app, db, login_required
from flask import render_template, request

@app.route("/groups/own")
def groups_mine():
    return render_template("discussions/own.html")
