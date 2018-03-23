from application import app
from flask import render_template, request

@app.route("/users/new/")
def users_form():
    return render_template("users/new.html")

@app.route("/user/", methods=["POST"])
def users_create():
    print(request.form.get("name"))

    return "hello world!"
