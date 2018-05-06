from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.discussions.models import Discussion
from application.auth.models import Account
from application.groups.models import Groups
from application.groups.forms import GroupForm

@app.route("/groups/")
@login_required()
def groups_index():
    groups = Groups.find_usernames_for_all_discussion_owners()

    return render_template("group/index.html", groups = groups)

@app.route("/groups/<int:param>")
@login_required()
def group_home(param):
    group = Discussion.find_usernames_for_discussion_owners(param)
    if not group:
        return redirect(url_for("groups_index"), error = "That group does not exist")

    return render_template("group/index.html", discussions = group, target = param)

@app.route("/groups/new", methods=["GET"])
@login_required()
def groups_new():
    return render_template("group/new.html", form = GroupForm())

@app.route("/groups/new", methods=["POST"])
@login_required()
def groups_create():
    form = GroupForm(request.form)

    g = Groups(form.name.data, current_user.get_id())
    db.session().add(g)
    db.session().commit()

    return redirect(url_for("group_home", param = g.id))
