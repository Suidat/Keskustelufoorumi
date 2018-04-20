from application import db
from application.models import Base

class Message(Base):
    message = db.Column(db.Text, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('Group.id'), nullable = False)
    sender_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)

    def __init__(self, name, sender):
        self.message = name
        self.sender_id = sender
