from flask import render_template, request, redirect, url_for
from application import app, db, login_required
from application.groups.models import Groups
from application.discussions.models import Discussion
from application.forms import SearchForm

@app.route("/")
def index():
    groups = Groups.find_usernames_for_group_owners()

    return render_template("index.html", groups = groups, form = SearchForm())

@app.route("/search", methods = ["POST"])
@login_required()
def search():

    form = SearchForm(request.form)
    if not form.validate():
        groups = Groups.find_usernames_for_group_owners()
        return render_template("index.html", groups = groups, form = SearchForm(), error = "Please search for something")

    return redirect(url_for("search_results", param = request.form.get("search"), page = 1))


@app.route("/search/<param>/<int:page>")
@login_required()
def search_results(param, page):
    if page < 1:
        return redirect(url_for("search_results", param = param, page = 1))

    groups = Groups.search(param, page)
    discussions = Discussion.search(param, page)
    if (not groups or not discussions) and page != 1:
        return redirect(url_for("search_results", param = param, page = page-1))

    return render_template("search.html", groups = groups, discussions = discussions, current = page, param = param)
