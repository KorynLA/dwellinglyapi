import sqlite3
from flask_restful import Resource, reqparse
from flask import request

# | method | route                | action                     |
# | :----- | :------------------- | :------------------------- |
# | POST   | `v1/properties/`     | Creates a new property     |
# | GET    | `v1/properties/`     | Gets all properties        |
# | GET    | `v1/properties/:id` | Gets a single property     |
# | PATCH  | `v1/properties/:id` | Updates a single property  |
# | DELETE | `v1/properties/:id` | Deletes a single property  |



propertyList= [
     {
    "id": "property1",
    "name": "Garden Blocks",
    "address": "1654 NE 18th Ave.",
    "zipCode": "97218",
    "city": "Portland",
    "state": "OR"
  },
  {
    "id": "property2",
    "name": "Magnolia Park",
    "address": "2200 SE Main St.",
    "zipCode": "12340",
    "city": "Portland",
    "state": "OR"
  },
  {
    "id": "property3",
    "name": "Mountain View",
    "address": "311 Sandy Blvd.",
    "zipCode": "97218",
    "city": "Portland",
    "state": "OR"
  }
]


# single property resource
class Property(Resource):

    def get(self,id):
        rentalProperty = self.find_by_id(id) 
        if rentalProperty:
            return rentalProperty
        else:
            return {'message': 'Property Not Found'}, 404

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM properties WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'property': {'id': row[0], 'name': row[1], 'address': row[2], 'zipCode': row[3], 'city': row[4], 'state': row[5]}}
        return {'message': 'Property Not Found'}, 404
    
    def post(self, id):
        if self.find_by_id(id):
            return {'message': "A property with the id '{}' already exists".format(id)}, 400
        parser = reqparse.RequestParser()
        data = parser.parse_args()
        rentalproperty = {id: id, name: data['name'], address: data['address'], zipCode: data['zipCode'], city: data['city'], state: data['state']}
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
    def patch(self,id):
        property = next(filter(lambda x: x["id"] == id, propertyList), None)
        # request_data = request.get_json()
        #   "id": "property-01",

        # "name": "Garden Blocks",
        # "address": "1654 NE 18th Ave.",
        # "zipCode": "97218",
        # "city": "Portland",
        # "state": "OR"

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
        global propertyList
        propertyList = next(filter(lambda x: x["id"] != id, propertyList), None)
        return {"message": "property deleted"}

class Properties(Resource):
    def get(self):
        return {"properties": propertyList}, 200 if propertyList else 404

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
