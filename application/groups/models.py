from application import db
from application.models import Base

class Group(Base):
    __tablename__ = 'Group'
    name = db.Column(db.String(144), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
