from flask_login import current_user
from flask import render_template, request, redirect, url_for

from application import app, db, login_required
from application.messages.models import Message
from application.messages.forms import MessageForm

@app.route("/discussions/<int:target>/new/", methods=["POST"])
@login_required()
def messages_create(target):

    m = Message(request.form.get("message"), target, current_user.get_id())
    db.session().add(m)
    db.session().commit()

    return redirect(url_for("discussion_home", target = target))


@app.route("/message/delete/<int:param>")
@login_required()
def message_delete(param):

    toDelete = Message.query.filter_by(id = param).first()
    if toDelete.sender_id == current_user.get_id():
        Message.delete_message_with_id(param)
    return redirect(url_for("discussion_home", target = toDelete.discussion_id))
