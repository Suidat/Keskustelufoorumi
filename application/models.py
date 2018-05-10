from application import db

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

class GroupAccountLink(Base):

    __tablename__ = "Linkag"

    group_id = db.Column(db.Integer, db.ForeignKey('Groups.id'), nullable = False)
    account_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)
    banned = db.Column(db.Boolean, nullable = False)

    def __init__(self, group_id, account_id, ban):
        self.group_id = group_id
        self.account_id = account_id
        self.banned = ban

    def get_status(self):
        return self.banned

    def get_user(self):
        return self.account_id

    def get_group(self):
        return self.group_id

    def change_status(self):
        if self.banned:
            self.banned = False
        else:
            self.banned = True
