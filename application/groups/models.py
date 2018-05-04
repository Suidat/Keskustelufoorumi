from application import db
from application.models import Base

class Groups(Base):
    __tablename__ = 'Groups'
    name = db.Column(db.String(144), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
