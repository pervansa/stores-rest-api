from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # truring off the tracking modification
app.secret_key = 'pervez'
api = Api(app)



jwt = JWT(app, authenticate, identity) # jwt create a new endpoints /auth, intialize the JWT object 




api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db

    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True) 

    # with app.app_context():
    #     db.create_all()
    