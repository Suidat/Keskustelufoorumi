from application import db
from application.models import Base
from sqlalchemy.sql import text

class Groups(Base):
    __tablename__ = 'Groups'
    name = db.Column(db.String(144), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)

    def __init__(self, name, owner):
        self.name = name
        self.owner_id = owner

    @staticmethod
    def find_usernames_for_group_owners():
        stmt = text("SELECT Account.name as username, Groups.* from Account, Groups WHERE Account.id = GROUPS.owner_id")
        res = db.engine.execute(stmt)
        return res
