from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy_utils import database_exists, create_database

db_url = "postgresql://postgres:postgres@localhost:5432/Riddles"

if not database_exists(db_url):
    create_database(db_url)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SECRET_KEY'] = '2a2f075acf6a18bd4612bf420066a533'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from project import routes