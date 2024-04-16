from flask import Flask
from flask_restful import Api
from config import db
from routes import Signup, CheckSession, Login, Logout, RecipeIndex

app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)

# Define routes for each resource
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
