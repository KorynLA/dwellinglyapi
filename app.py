from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models.user import UserModel
from resources.user import UserRegister, User, UserLogin
from resources.property import Properties, Property
from functools import wraps
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

@jwt.user_claims_loader
def role_loader(identity):
    user = UserModel.find_by_id(identity)
    if user.role == 'admin':
        return{'is_admin': True}
    return {'is_admin': False}

#custom decorator, JWT is present + user has admin permissions
def user_is_admin(fn):
	@wraps(fn)
	def admin_wrapper(*args, **kwargs):
		verify_jwt_in_request()
		user_admin_claim=get_jwt_claims()
		if(user_admin_claim[is_admin]):
			return fn(*args, **kwargs)
		else:
			return {"message":"Action is not Authorized"}, 403
	return admin_wrapper


api.add_resource(UserRegister, '/register')
api.add_resource(Property,'/properties/<string:name>')
api.add_resource(Properties,'/properties')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    # db.init_app(app) 
    app.run(port=5000, debug=True)