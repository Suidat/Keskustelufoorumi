from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from application.auth.models import Account
from application.auth.forms import AccountForm, LoginForm

@app.route("/user/new/")
def users_form():
    return render_template("user/new.html")

@app.route("/user/new/", methods=["POST"])
def users_create():
    u = Account(request.form.get("user_name"), request.form.get("password"))
    db.session().add(u)
    db.session().commit()

    return render_template("user/own")

@app.route("/user/own")
def users_own():
    return render_template("user/own")

@app.route("/user/login")
def auth_login():
    if request.method == "GET":
        return render_template("users/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("users/loginform.html", form = form,
                                error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))



@app.route("/user/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
