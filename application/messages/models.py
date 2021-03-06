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

    def get_message(self):
        return self.message

    @staticmethod
    def find_messages_with_usernames(param, page):
        per_page = 10
        stmnt = text("SELECT Account.name AS username, Message.* FROM Account, Message WHERE Account.id=Message.sender_id AND Message.discussion_id = :disc ORDER BY Message.date_created ASC LIMIT 10 OFFSET :page").params(disc = param, page = (page*per_page-10))
        res = db.engine.execute(stmnt)
        result = []
        for r in res:
            result.append(r)
        return result

    @staticmethod
    def delete_message_with_id(toDelete):
        stmt = text("DELETE FROM Message WHERE id = :id").params(id = toDelete)
        db.engine.execute(stmt)
        db.session.commit()

    @staticmethod
    def edit_message_with_id(id, edit):
        stmt  = text("UPDATE Message SET message = :edit WHERE id = :id").params(edit = edit, id = id)
        db.engine.execute(stmt)
        db.session.commit()
