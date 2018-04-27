from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.discussions.forms import DiscussionForm
from application.discussions.models import Discussion

@app.route("/discussions/")
def discussions_index():

    return render_template("discussions/index.html")


@app.route("/groups/<int:param>/new", methods=["POST", "GET"])
def discussions_new(param):
    if request.method == "GET":
        if current_user.is_authenticated:
            return render_template("discussions/new.html", form = DiscussionForm())
        else:
             return redirect(url_for("discussions_index"))

    d = Discussion(request.form.get("name"), param, current_user.user_id)
    db.session().add(d)
    db.session().commit()

    return render_template("discussions/index.html")
