import datetime
from db import db

class TicketsModel(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    issue =  db.Column(db.String(200))
    sent = Column(DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20))
    urgency = db.Column(db.String(20)) 
    tenentID = db.Column(db.Integer, db.ForeignKey('user.id'))
    senderID = db.Column(db.Integer, db.ForeignKey('user.id'))
    supportID = db.Column(db.Integer, db.ForeignKey('user.id'))
    notes = db.relationship('ticketnotesModel')
    users = db.relationship('userModel')

    def __init__(self, id, issue, sent, status, urgency, tenentID, senderID, supportID, notes):
        self.id = id
        self.issue = issue
        self.sent = sent
        self.status = status
        self.urgency = urgency
        self.tenentID = tenentID
        self.senderID = senderID
        self.supportID = supportID
        self.notes = notes
    
    def json(self):
        return {'id': self.id, 'issue':self.issue, 'sent': sent, 'status': self.status, 'urgency': self.urgency, 'tenent': self.tenent, 'sender': self.sender, 'notes': [notes.json() for note in self.notes.all()]}
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() #SELECT * FROM property WHERE id = id LIMIT 1
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
