from application import app
from flask import render_template, request

@app.route("/discussions/")
def discussions_index():
    return render_template("discussions/index.html")
