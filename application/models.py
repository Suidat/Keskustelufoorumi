from application import db

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

class GroupAccountLink(Base):

    group_id = db.Column(db.Integer, db.ForeignKey('Groups.id'), nullable = False)
    account_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)

    def __init__(self, group_id, account_id):
        self.group_id = group_id
        self.account_id = account_id
