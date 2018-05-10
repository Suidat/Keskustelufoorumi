from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from application.auth.models import Account
from application.auth.forms import AccountForm, LoginForm, EditForm
from application.groups.models import Groups
from application.discussions.models import Discussion

@app.route("/user/new")
def users_form():
    return render_template("users/new.html", form = AccountForm())

@app.route("/user/new", methods=["POST"])
def users_create():
    u = Account(request.form.get("username"), request.form.get("password"))

    db.session().add(u)
    db.session().commit()

    return render_template("users/loginform.html", form = LoginForm(), error = "Please login to complete signup")

@app.route("/user/own")
@login_required()
def user_own():
    groups = Groups.find_owned_groups(current_user.get_id())
    discussions = Discussion.find_owned_discussions(current_user.get_id())
    form = EditForm()
    return render_template("users/own.html", groups = groups, discussions = discussions , form = form)

@app.route("/user/edit", methods = ["POST"])
@login_required()
def user_edit():
    p1 = request.form.get("password_new1")
    p2 = request.form.get("password_new2")
    pold = request.form.get("password_old")
    old = Account.query.filter_by(id = current_user.get_id()).first()
    if old.password == pold:
        if p1 == p2:
            Account.change_password(p1, current_user.get_id())
    return redirect(url_for("user_own"))

@app.route("/user/login", methods =["POST", "GET"])
def auth_login():
    if request.method == "GET":
        return render_template("users/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = Account.query.filter_by(name=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("users/loginform.html", form = form,
                                error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/user/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
