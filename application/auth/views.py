from application import app
from flask import render_template, request

@app.route("/user/new/")
def users_form():
    return render_template("user/new.html")

@app.route("/user/new/", methods=["POST"])
def users_create():
    print(request.form.get("name"))

@app.route("/user/own")
def users_own():
    return render_template("user/own")
