from application import db
from application.models import Base
from sqlalchemy.sql import text


class Message(Base):
    __tablename__ = "Message"
    message = db.Column(db.Text, nullable=False)
    discussion_id = db.Column(db.Integer, db.ForeignKey('Discussion.id'), nullable = False)
    sender_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)

    def __init__(self, name, discusson ,sender):
        self.message = name
        self.discussion_id = discusson
        self.sender_id = sender

    @staticmethod
    def find_messages_with_usernames(param):
        stmnt = text("SELECT Account.name AS username, Message.* FROM Account, Message WHERE Account.id=Message.sender_id AND Message.discussion_id = :disc").params(disc = param)
        res = db.engine.execute(stmnt)

        return res
    @staticmethod
    def delete_message_with_id(toDelete):
        stmt = text("DELETE FROM Message WHERE Message.id = :id").params(id = toDelete)
        db.engine.execute(stmt)
        
