from application import db
from application.models import Base

class Account(Base):
    __tablename__ = 'Account'
    name = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(5), default="User")

    def __init__(self, name, password, r):
        self.name = name
        self.password = password
        self.role = r

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
