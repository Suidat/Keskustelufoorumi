from application import db
from application.models import Base

class Discussion(Base):
    __tablename__ = 'Discussion'
    name = db.Column(db.String(144), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('Group.id'), nullable = False)
    owner_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)


    def __init__(self, name):
        self.name = name
