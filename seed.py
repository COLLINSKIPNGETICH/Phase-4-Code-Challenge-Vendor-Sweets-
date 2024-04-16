from flask import Flask
from config import db
from models import User, Recipe

# Initialize the Flask application context
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Initialize the database
db.init_app(app)

def seed_database():
    with app.app_context():
        # Seed data creation (example)
        user1 = User(username='user1', password='password1')
        user2 = User(username='user2', password='password2')
        db.session.add(user1)
        db.session.add(user2)

        recipe1 = Recipe(title='Recipe 1', instructions='Instructions 1', minutes_to_complete=30, user=user1)
        recipe2 = Recipe(title='Recipe 2', instructions='Instructions 2', minutes_to_complete=45, user=user2)
        db.session.add(recipe1)
        db.session.add(recipe2)

        db.session.commit()

if __name__ == '__main__':
    seed_database()
