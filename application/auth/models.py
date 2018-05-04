from application import db
from application.models import Base

class Account(Base):
    __tablename__ = 'Account'
    name = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
