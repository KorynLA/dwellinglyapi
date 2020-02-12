from flask_restful import Resource
from models.tenents import TenentsModel

class Tenent(Resource):
    def get(self, id):
        tenent = TenentModel.find_by_id(id)
        if tenent:
            return tenent.json()
        return {'message': 'Tenent Not Found'}, 404
    
    def post(self,id):
        if TenentModel.find_by_id(id):
            return('message': 'Tenent already exists'), 400
        
        tenent = TenentModel(id)
        try:
            tenent.save_to_db()
        except:
            return {'Message': 'An Error Has Occured'}, 500

        return tenent.json(), 201

    def delete(self, id):
        tenent = TenentModel.find_by_id(id)
        if tenent:
            tenent.delete_from_db()

        return{'Message': 'Tenent Removed from Database'}

class Tenents(Resource):
    def get(self):
        return {'Tenents': [tenent.json() for tenent in TenentModel.query.all()]}
