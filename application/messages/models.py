from application import db
from application.models import Base

class Message(Base):
    __tablename__ = "Message"
    message = db.Column(db.Text, nullable=False)
    discussion_id = db.Column(db.Integer, db.ForeignKey('Discussion.id'), nullable = False)
    sender_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)

    def __init__(self, name, sender):
        self.message = name
        self.sender_id = sender
