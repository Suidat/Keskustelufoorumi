from flask import render_template, request, redirect, url_for

from application import app, db
from application.messages.models import Message
from application.messages.forms import MessageForm

@app.route("/messages/new/")
def messages_form():
    return render_template("messages/new.html", form = MessageForm())
