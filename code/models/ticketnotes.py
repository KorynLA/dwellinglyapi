import datetime
from db import db

class TicketsNotesModel(db.Model):
    __tablename__ = "ticketnotes"

    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(256))
    sent = Column(DateTime, default=datetime.datetime.utcnow)
    db.relationship('TicketsModel', lazy='dynamic')
    db.relationship('UserModel', lazy='dynamic')

    def __init__(self, userID, sent, message):
        self.id = id
        self.sent = sent
        self.userID = userID
        self.message = message
    

    def json(self):
        return {'id': self.id, 'userID':self.userID, 'message': self.message, 'sent': self.sent}
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() #SELECT * FROM property WHERE id = id LIMIT 1
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
