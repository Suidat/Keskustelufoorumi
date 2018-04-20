from application import app, db, login_required
from flask import render_template, request

@app.route("/discussions/")
def discussions_index():
    return render_template("discussions/index.html")


@app.route("/discussions/")
def discussions_mine():
    return render_template("discussions/index.html")
