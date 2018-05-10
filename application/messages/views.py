from flask_login import current_user
from flask import render_template, request, redirect, url_for

from application import app, db, login_required
from application.messages.models import Message
from application.messages.forms import MessageForm
from application.discussions.models import Discussion
from application.models import GroupAccountLink

@app.route("/discussions/<int:target>/new/", methods=["POST"])
@login_required()
def messages_create(target):
    discussion = Discussion.query.filter_by(id = target).first()
    banned = GroupAccountLink.query.filter_by(account_id = current_user.get_id(), group_id = discussion.group_id).first()
    if not banned:
        return redirect(url_for("group_home", param = discussion.group_id))
    elif banned.get_status():
        return redirect(url_for("index"))


    m = Message(request.form.get("message"), target, current_user.get_id())
    db.session().add(m)
    db.session().commit()
    return redirect(url_for("discussion_home", target = target))


@app.route("/message/delete/<int:param>")
@login_required()
def message_delete(param):
    message = Message.query.filter_by(id = param).first()
    discussion = Discussion.query.filter_by(id = message.discussion_id).first()
    banned = GroupAccountLink.query.filter_by(account_id = current_user.get_id(), group_id = discussion.group_id).first()
    if not banned:
        return redirect(url_for("group_home", param = discussion.group_id))
    elif banned.get_status():
        return redirect(url_for("index"))

    toDelete = Message.query.filter_by(id = param).first()
    if toDelete.sender_id == current_user.get_id():
        Message.delete_message_with_id(param)
    return redirect(url_for("discussion_home", target = toDelete.discussion_id))

@app.route("/message/edit/<int:param>", methods=["POST", "GET"])
@login_required()
def message_edit(param):
    message = Message.query.filter_by(id = param).first()
    discussion = Discussion.query.filter_by(id = message.discussion_id).first()
    banned = GroupAccountLink.query.filter_by(account_id = current_user.get_id(), group_id = discussion.group_id).first()
    if not banned:
        return redirect(url_for("group_home", param = discussion.group_id))
    elif banned.get_status():
        return redirect(url_for("index"))

    toEdit = Message.query.filter_by(id = param).first()
    if request.method == "GET":
        f = MessageForm()
        f.message.data = toEdit.get_message()
        return render_template("discussions/edit.html", form = f, id = param)

    if toEdit.sender_id == current_user.get_id():
        Message.edit_message_with_id(param, request.form.get("message"))
    return redirect(url_for("discussion_home", target = toEdit.discussion_id))
