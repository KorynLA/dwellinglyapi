import datetime
from db import db

class LeaseModel(db.Model):
    __tablename__ = "lease"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    unit = db.Column(db.String(20))
    dateStart = Column(DateTime, default=datetime.datetime.utcnow)
    dateEnd = Column(DateTime, default=datetime.datetime.utcnow)
    dateUpdated = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, id, name, unit, dateStart, dateEnd, dateUpdated):
        self.id = id
        self.name = name
        self.unit = unit
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.dateUpdate = dateUpdated
    

    def json(self):
        return {'id': self.id, 'name':self.name, 'unit': unit, 'dateStart': self.dateStart, 'dateEnd': self.dateEnd, 'dateUpdate': self.dateUpdated}
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() #SELECT * FROM property WHERE id = id LIMIT 1
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

