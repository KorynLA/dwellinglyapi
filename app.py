from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import UserRegister, User, UserLogin
from resources.property import Properties, Property

from db import db


app = Flask(__name__)
#config DataBase
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'dwellingly' #Replace with Random Hash

api = Api(app)

db.init_app(app) #need to solve this 

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app) # /authorization 

api.add_resource(UserRegister, '/register')
api.add_resource(Property,'/properties/<string:name>')
api.add_resource(Properties,'/properties')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    # db.init_app(app) 
    app.run(port=5000, debug=True)