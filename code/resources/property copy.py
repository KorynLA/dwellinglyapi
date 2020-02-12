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
    def get(self):
        return "Property is up and Running"

class Properties(Resource):
    def get(self):
        return {'properties': [property.json() for property in PropertyModel.query.all()]}

    def post(self):
        
        request_data = request.get_json()

        new_property = {
          "id":id,
          "name": request_data["name"],
          "address": request_data["address"],
          "zipCode": request_data["zipCode"],
          "city": request_data["city"],
          "state": request_data["state"]
          }
          
        return new_property, 201
