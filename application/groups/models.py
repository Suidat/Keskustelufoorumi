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

    @staticmethod
    def find_owned_groups(arg):
        stmt= text("SELECT Groups.*, Account.name as username From Groups, Account WHERE Groups.owner_id = Account.id AND Account.id = :id").params(id = arg)
        res = db.engine.execute(stmt)
        return res

    @staticmethod
    def edit_group(n, gid):
        stmt = text("UPDATE Groups SET name = :arg WHERE id = :id").params(arg = n, id = gid)
        res = db.engine.execute(stmt)
        db.session.commit()
        return res

    @staticmethod
    def search(arg, page):
        search = '%'+arg+'%'
        per_page = 10
        stmt = text("SELECT * FROM Groups WHERE name LIKE :param ORDER BY date_created ASC LIMIT 10 OFFSET :page").params(param = search, page = (page*per_page-10))
        res = db.engine.execute(stmt)
        return res
