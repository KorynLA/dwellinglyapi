import datetime
from db import db

class TenentsModel(db.Model):
    __tablename__ = "tenents"

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    property = db.relationship('PropertyModel', lazy='dynamic')
    lease_id = db.Column(db.Integer, db.ForeignKey('lease.id'))
    lease = db.relationship('LeaseModel', lazy='dynamic')


    def __init__(self, id, firstName, lastName, phone, property, lease):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.property = property
        self.lease = lease
    

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


# tenentsList = [
#     {
#     "id": "tenent1",
#     "dateCreated": "Thu Aug 23 2018 16:40:35 GMT-0700 (Pacific Daylight Time)",
#     "dateUpdated": "Thu Aug 23 2018 15:54:48 GMT-0700 (Pacific Daylight Time)",
#     "lastName": "Smith",
#     "firstName": "Will",
#     "phone": "503-555-1234",
#     "lease": "LEASE2",
#     "propertyid": "property1"
#     },
#     {
#     "id": "tenent2",
#     "dateCreated": "Thu Aug 24 2018 16:40:35 GMT-0700 (Pacific Daylight Time)",
#     "dateUpdated": "Thu Aug 24 2018 15:54:48 GMT-0700 (Pacific Daylight Time)",
#     "lastName": "Bluth",
#     "firstName": "George",
#     "phone": "503-555-1235",
#     "lease": "LEASE1",
#     "propertyid": "property2"
#     }
# ]
