from flask_restful import Resource, reqparse
from db import db
from models.property import PropertyModel

# | method | route                | action                     |
# | :----- | :------------------- | :------------------------- |
# | POST   | `v1/properties/`     | Creates a new property     |
# | GET    | `v1/properties/`     | Gets all properties        |
# | GET    | `v1/properties/:id` | Gets a single property     |
# | PATCH  | `v1/properties/:id` | Updates a single property  |
# | DELETE | `v1/properties/:id` | Deletes a single property  |

# single property resource
class Property(Resource):

    def get(self,id):
        rentalProperty = PropertyModel.find_by_id(id) 
        if rentalProperty:
            return rentalProperty.json()
        else:
            return {'message': 'Property Not Found'}, 404

    def post(self, id):
        if PropertyModel.find_by_id(id):
            return {'message': "A property with the id '{}' already exists".format(id)}, 400
        parser = reqparse.RequestParser()
        data = parser.parse_args()
        rentalproperty = {'id': id, 'name': data['name'], 'address': data['address'], 'zipCode': data['zipCode'], 'city': data['city'], 'state': data['state']}
        try:
            PropertyModel.save_to_db(rentalproperty)
        except:
            return{"Message": "An Error has Occured"}, 500

        return rentalproperty, 201
    
    def put(self, id):
        data = parser.parse_args()

        property = PropertyModel.find_by_id(id)
        # updated_property = {'id': id, 'name': data['name'], 'address': data['address'], 'zipCode': data['zipCode'], 'city': data['city'], 'state': data['state']}
        if property is None:
            property = PropertyModel(id, **data)
        else:
            property.name = data['name']
            property.address = data['address']
            property.city = data['city']
            property.state = data['state']
            property.zipCode = data['zipCode']

        property.save_to_db()

        return property.json(), 201

        
    def patch(self,id):
        property = PropertyModel.find_by_id(id)

        parser = reqparse.RequestParser()
        parser.add_argument('name', help="need a name")
        parser.add_argument('address', help="address incomplete")
        parser.add_argument('city', help="address incomplete")
        parser.add_argument('zipCode', help="address incomplete")
        parser.add_argument('state', help="address incomplete")

        request_data = parser.parse_args()

        if property:
            property.update(request_data)
        return {"property": property}, 200

    def delete(self, id):
        property = PropertyModel.find_by_id(id)
        if property:
            property.delete_from_db()
        return {"message": "property deleted"}

class Properties(Resource):
    def get(self):
        return {'properties': [property.json() for property in PropertyModel.query.all()]}

    def post(self):
        id = "property" + str(len(propertyList)) 
        request_data = request.get_json()

        new_property = {
          "id":id,
          "name": request_data["name"],
          "address": request_data["address"],
          "zipCode": request_data["zipCode"],
          "city": request_data["city"],
          "state": request_data["state"]
          }
        propertyList.append(new_property)

        return new_property, 201
