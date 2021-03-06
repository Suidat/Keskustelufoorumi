from application import db
from application.models import Base
from sqlalchemy.sql import text


class Discussion(Base):
    __tablename__ = 'Discussion'
    name = db.Column(db.String(144), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('Groups.id'), nullable = False)
    owner_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)


    def __init__(self, name, group, owner):
        self.name = name
        self.group_id = group
        self.owner_id = owner

    @staticmethod
    def delete_discussion_and_messages(arg):
        stmt = text("DELETE FROM Discussion WHERE id = :id; DELETE FROM Message WHERE discussion_id = :id").params(id = arg)
        db.engine.execute(stmt)
        db.session.commit()


    @staticmethod
    def find_owned_discussions(arg):
        stmt = text("SELECT Discussion.*, Account.id as user_id, COUNT(Message.id) AS amount FROM Account, Discussion LEFT OUTER JOIN Message ON Discussion.id = Message.discussion_id WHERE Discussion.owner_id = Account.id AND Account.id = :id GROUP BY Discussion.id").params(id = arg)
        res = db.engine.execute(stmt)
        return res

    @staticmethod
    def find_usernames_for_all_discussion_owners():
        stmt = text("SELECT Account.name as username, Discussion.* from Account, Discussion WHERE Account.id = Discussion.owner_id")
        res = db.engine.execute(stmt)
        return res

    @staticmethod
    def find_usernames_for_discussion_owners(param):
        stmt = text("SELECT Account.name as username, Discussion.* from Account, Discussion WHERE Account.id = Discussion.owner_id AND Discussion.group_id = :id ").params(id = param)
        res = db.engine.execute(stmt)
        return res

    @staticmethod
    def search(arg, page):
        search = '%'+arg+'%'
        per_page = 10
        stmt = text("SELECT * FROM Discussion WHERE name LIKE :param ORDER BY date_created ASC LIMIT 10 OFFSET :page").params(param = search, page = (page*per_page-10))
        res = db.engine.execute(stmt)
        return res
