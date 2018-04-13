from application import db

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class GroupAccountLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('Group.id'), nullable = False)
    account_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)

    def __init__(self, group_id, account_id):
        self.group_id = group_id
        self.account_id = account_id
