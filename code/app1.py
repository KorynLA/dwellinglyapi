from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.property import Property, Properties
from db import db

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# if __name__ == '__main__':
#     from db import db
#     db.init_app(app)
#     app.run(port=5000, debug=True)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

app.secret_key = "Dwellingly"  # could do app.config['JWT_SECRET_KEY'] if we prefer
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()
    
api.add_resource(Properties, "/v1/properties")
api.add_resource(Property, "/v1/properties/<string:id>")

if __name__ == '__main__':
    from db import db #circular imports requires db to be imported here
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True