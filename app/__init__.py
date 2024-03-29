from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialises the app
app = Flask(__name__)
app.config.from_object(Config)

# Initialises the database
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# Initialises the login
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models