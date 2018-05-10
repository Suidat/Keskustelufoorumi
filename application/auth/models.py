from application import db
from application.models import Base
from sqlalchemy.sql import text

class Account(Base):
    __tablename__ = 'Account'
    name = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(5), default="User")


    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.role = "User"
        if self.id==1:
            self.role = "Admin"

    def role(self):
        return self.role

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def change_password(arg, user_id):
        stmt = text("UPDATE Account SET password = :password WHERE id = :user").params(password = arg, user = user_id)
        db.engine.execute(stmt)
        db.session.commit()

    @staticmethod
    def find_usernames_for_members(param):
        stmt = text("SELECT Account.id, Account.name As username, Linkag.group_id, Linkag.banned FROM Account, Linkag Where Linkag.account_id = Account.id AND Linkag.group_id = :id").params(id = param)
        res = db.engine.execute(stmt)
        return res
