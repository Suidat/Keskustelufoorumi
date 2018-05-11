from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from application.models import GroupAccountLink
from application.discussions.models import Discussion
from application.auth.models import Account
from application.groups.models import Groups
from application.groups.forms import GroupForm

@app.route("/groups/")
@login_required()
def groups_index():
    groups = Groups.find_usernames_for_all_discussion_owners()

    return render_template("group/index.html", groups = groups, error = error)

@app.route("/groups/<int:param>")
@login_required()
def group_home(param):
    group = Groups.query.filter_by(id=param).first()
    if not group:
        groups = Groups.find_usernames_for_group_owners()
        return render_template("index.html", groups = groups, error = "That group does not exist")

    stat = GroupAccountLink.query.filter_by(account_id = current_user.get_id(), group_id = param).first()

    if not stat:
        s = False
    elif stat.get_status():
        groups = Groups.find_usernames_for_group_owners()
        return render_template("index.html", groups = groups, error = "You are banned from this group")
    else:
        s = True

    mem = Account.find_usernames_for_members(param)

    disc = Discussion.find_usernames_for_discussion_owners(param)
    return render_template("group/index.html", discussions = disc, target = param, status = s, members = mem, group_owner = group.owner_id)

@app.route("/groups/new", methods=["GET"])
@login_required()
def groups_new():
    return render_template("group/new.html", form = GroupForm())

@app.route("/groups/new", methods=["POST"])
@login_required()
def groups_create():
    form = GroupForm(request.form)
    if not form.validate():
        return render_template("group/new.html", form = GroupForm(), error = "Minimum length for name is 4")
    g = Groups(form.name.data, current_user.get_id())
    db.session().add(g)
    db.session().commit()
    ga = GroupAccountLink(g.id, current_user.get_id(), False)
    db.session().add(ga)
    db.session().commit()

    return redirect(url_for("group_home", param = g.id))

@app.route("/groups/ban/<int:group>/<int:toBan>")
@login_required()
def ban_user(toBan, group):
    group = Groups.query.filter_by(id = current_user.get_id()).first()
    if current_user.get_id() != group.owner_id:
        return redirect(url_for("group_home", param = group.id))

    ban = GroupAccountLink.query.filter_by(account_id = toBan).first()
    if not ban:
        return redirect(url_for("group_home", param = group.id))

    ban.banned = True

    return redirect(url_for("group_home", param = group.id))

@app.route("/groups/ban/<int:group>/<int:toBan>")
@login_required()
def unban_user(toBan, group):
    group = Groups.query.filter_by(id = current_user.get_id()).first()
    if current_user.get_id() != group.owner_id:
        return redirect(url_for("group_home", param = group))

    ban = GroupAccountLink.query.filter_by(account_id = toBan).first()
    if not ban:
        return redirect(url_for("group_home", param = group))
    elif ban.banned:
        ban.banned = False

    return redirect(url_for("group_home", param = group))

@app.route("/groups/edit/<int:param>", methods = ["POST", "GET"])
@login_required()
def group_edit(param):
    toEdit = Groups.query.filter_by(id = param).first()
    if request.method == "GET":
        form = GroupForm()
        form.name.data = toEdit.name
        return render_template("group/edit.html", form = form, id = param)

    form = GroupForm(request.form)
    if not form.validate():
        return render_template("group/edit.html", form = form, error = "Minimum length for name is 4
    Groups.edit_group(form.name.data, param)


    return redirect(url_for("user_own"))


@app.route("/groups/join/<int:param>")
@login_required()
def group_join(param):
    ga = GroupAccountLink.query.filter_by(group_id=param, account_id = current_user.get_id()).first()
    if not ga:
        ga = GroupAccountLink(param, current_user.get_id(), False)
        db.session().add(ga)
        db.session().commit()
    elif ga.get_status():
        return redirect(url_for("index", error = "You are banned from this group"))

    return redirect(url_for("group_home", param = param))
