from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Flask App Configuration
DEBUG = True
SECRET_KEY = 'your_secret_key_here'

# SQLAlchemy Configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Bcrypt Configuration
BCRYPT_LOG_ROUNDS = 12

# Initialize Flask Extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
