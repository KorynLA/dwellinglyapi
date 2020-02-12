from db import db

class PropertyModel(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(250))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zipcode = db.column(db.String(20))

    # renterID = db.Column(db.Integer, db.ForeignKey('users.id'))
    # renter = db.relationship('UserModel', lazy='dynamic')


    def __init__(self, id, name, address, city, state, zipcode, renterID):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.renterID = renterID
    

    def json(self):
        return {'id': self.id, 'name':self.name, 'address': self.address, 'city': self.city, 'state': self.state}
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() #SELECT * FROM property WHERE id = id LIMIT 1
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
