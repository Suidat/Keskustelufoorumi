from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.discussions.forms import DiscussionForm
from application.models import GroupAccountLink
from application.discussions.models import Discussion
from application.messages.forms import MessageForm
from application.messages.models import Message

@app.route("/discussions/<int:target>")
@login_required()
def discussion_home(target):
    discussion = Discussion.query.filter_by(id = target).first()
    banned = GroupAccountLink.query.filter_by(account_id = current_user.get_id(), group_id = discussion.group_id).first()
    if not banned:
        return redirect(url_for("group_home", param = discussion.group_id))
    elif banned.get_status():
        return redirect(url_for("index"))

    disc = Message.find_messages_with_usernames(target)
    return render_template("discussions/index.html", messages = disc, form = MessageForm(), target = target)


@app.route("/groups/<int:param>/new", methods=["POST", "GET"])
@login_required()
def discussions_new(param):

    banned = GroupAccountLink.query.filter_by(account_id = current_user.get_id(), group_id = param).first()
    if not banned:
        return redirect(url_for("group_home", param = param))
    elif banned.get_status():
        return redirect(url_for("index"))

    if request.method == "GET":
        if current_user.is_authenticated:
            return render_template("discussions/new.html", form = DiscussionForm(), param = param)
        else:
             return redirect(url_for("index"))

    d = Discussion(request.form.get("name"), param, current_user.get_id())
    db.session().add(d)
    db.session().commit()

    return redirect(url_for("discussion_home", target = param))
