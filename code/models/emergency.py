from db import db

class EmergencyModel(db.Model):
    __tablename__ = "emergency"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    emergencytype = db.Column(db.String(20))
    number = db.column(db.string(12))
    userid = db.Column(db.String(20), db.ForeignKey('users.id'))
    user = db.relationship('UserModel', lazy='dynamic')
    propertyid = db.Column(db.String(100) db.ForeignKey('property.id'))
    property = db.relationship('PropertyModel', lazy='dynamic')
    
    def __init__(self, id, name, emergencytype, number, userid, user, propertyid, propertytype):
        self.id = id
        self.name = name
        self.emergencytype = emergencytype
        self.number = number
        self.userid = userid
        self.propertytype = propertytype
    

    def json(self):
        return {'id': self.id, 'name':self.name, 'type': type, 'number': self.number, 'userid': self.userid, 'property': self.property}
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() #SELECT * FROM property WHERE id = id LIMIT 1
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


# emergencyList = [
#     {
#         "id": "00000001",
#         "name": "Test Number 1",
#         "type": "user",
#         "userid": "user1",
#         "propertyid":"none",
#         "number": "555-55-1234"
#     },
#       {
#         "id": "00000002",
#         "name": "Test Number 2",
#         "type": "property",
#         "userid": "none",
#         "propertyid":"property1",
#         "number": "555-55-1234"
#     }
# ]