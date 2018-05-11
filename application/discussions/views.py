from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.discussions.forms import DiscussionForm
from application.models import GroupAccountLink
from application.discussions.models import Discussion
from application.messages.forms import MessageForm
from application.groups.models import Groups
from application.messages.models import Message

@app.route("/discussions/<int:target>/<int:page>")
@login_required()
def discussion_home(target, page=1):
    if page < 1:
        return redirect(url_for("discussion_home", target = target, page = 1))
    d = Discussion.query.filter_by(id = target).first()
    check_ban(d.group_id)

    disc = Message.find_messages_with_usernames(target, page)
    if not disc and page != 1:
        return redirect(url_for("discussion_home", target = target, page = page-1))

    group = Groups.query.filter_by(id = target).first()
    f = False
    if page is 1:
        f = True

    return render_template("discussions/index.html", messages = disc, form = MessageForm(), target = target, ownerID = group.owner_id, First = True, current = page)


@app.route("/groups/<int:param>/new", methods=["POST", "GET"])
@login_required()
def discussions_new(param):
    check_ban(param)

    if request.method == "GET":
        if current_user.is_authenticated:
            return render_template("discussions/new.html", form = DiscussionForm(), param = param)
        else:
             return redirect(url_for("index"))
    d = Discussion(request.form.get("name"), param, current_user.get_id())
    db.session().add(d)
    db.session().commit()

    return redirect(url_for("discussion_home", target = d.id, page = 1))

#Checks to if user is banned from discussion
def check_ban(target):
        group = Groups.query.filter_by(id = target).first()
        banned = GroupAccountLink.query.filter_by(account_id = current_user.get_id(), group_id = group.id).first()
        if not banned:
            return redirect(url_for("group_home", param = discussion.group_id, page = 1))
        elif banned.get_status():
            return redirect(url_for("index"))
