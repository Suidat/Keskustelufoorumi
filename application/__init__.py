from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os
import psycopg2
if os.environ.get("HEROKU"):
    DATABASE_URL = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)


# login functionality
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                user_role = current_user.role()
                if user_role == role:
                    unauthorized = False


            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

#database creation and view imports
from application import views
from application.messages import views
from application.auth import views
from application.groups import views
from application.discussions import views
from application.auth import models
from application.groups import models
from application.discussions import models
from application.messages import models
from application import models

try:
    db.create_all()
except:
    pass

from application.auth.models import Account

@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(user_id)


#Go here for more information on this : http://www.gnuterrypratchett.com/
@app.after_request
def gnu_terry_pratchett(resp):
  resp.headers.add("X-Clacks-Overhead", "GNU Terry Pratchett")
  return resp
