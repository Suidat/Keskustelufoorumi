from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    message = db.Column(db.Text, nullable=False)

    group_id = db.Column(db.Integer, db.ForeignKey('Group.id'), nullable = False)
    sender_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable = False)

    def __init__(self, name, sender):
        self.message = name
        self.sender_id = sender
