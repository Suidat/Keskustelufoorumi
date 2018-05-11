from flask_login import current_user
from flask import render_template, request, redirect, url_for

from application import app, db, login_required
from application.messages.models import Message
from application.messages.forms import MessageForm
from application.discussions.models import Discussion
from application.models import GroupAccountLink
from application.discussions.views import check_ban

@app.route("/discussions/<int:target>/new/", methods=["POST"])
@login_required()
def messages_create(target):
    check_ban(target)
    form = MessageForm(request.form)
    if not form.validate():
        return render_template("discussions/edit.html", form = f, id = param, error = "Message too short. Minimum 2 characters")
    m = Message(request.form.get("message"), target, current_user.get_id())
    db.session().add(m)
    db.session().commit()
    return redirect(url_for("discussion_home", target = target, page = 1))


@app.route("/message/delete/<int:param>")
@login_required()
def message_delete(param):
    toDelete = Message.query.filter_by(id = param).first()
    d = Discussion.query.filter_by(id = toDelete.discussion_id).first()

    check_ban(d.id)
    g = Groups.query.filter_by(id = d.group_id)
    d_id = toDelete.discussion_id
    if toDelete.sender_id == current_user.get_id() or g.owner_id == current_user.get_id():
        Message.delete_message_with_id(param)
    return redirect(url_for("discussion_home", target = d_id))

@app.route("/message/edit/<int:param>", methods=["POST", "GET"])
@login_required()
def message_edit(param):
    toEdit = Message.query.filter_by(id = param).first()
    d = Discussion.query.filter_by(id = toEdit.discussion_id).first()
    check_ban(d.group_id)

    if toEdit.sender_id == current_user.get_id():
        if request.method == "GET":
            f = MessageForm()
            f.message.data = toEdit.get_message()
            return render_template("discussions/edit.html", form = f, id = param)
        form = MessageForm(request.form)
        if form.validate():
            Message.edit_message_with_id(param, request.form.get("message"))
            return redirect(url_for("discussion_home", target = toEdit.discussion_id))

        return render_template("discussions/edit.html", form = f, id = param, error = "Message too short. Minimum 2 characters")
