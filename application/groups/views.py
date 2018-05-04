from application import app, db, login_required
from flask import render_template, request
from flask_login import current_user

from application.discussions.models import Discussion
from application.groups.models import Groups
from application.groups.forms import GroupForm

@app.route("/groups/")
def groups_index():
    return render_template("group/index.html")

@app.route("/groups/<int:param>")
def group_home(param):
    group = Discussion.query.filter_by(group_id = param)
    if not group:
        return redirect(url_for("groups_index"), error = "That group does not exist")

    return render_template("discussions/index.html", discussions = group)

@app.route("/groups/new", methods=["POST","GET"])
@login_required()
def groups_new():
    if request.method == "GET":
        return render_template("group/new.html", form = GroupForm())

    form = GroupForm(request.form)
    if not form.validate():
        return render_template("group/new.html", form = form)
    g = Groups(form.name.data, current_user.get_id())
    db.session().add(g)
    db.session().commit()

    return redirect(url_for("groups/"++g.id))
