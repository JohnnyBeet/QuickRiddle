from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db_url = "postgresql://postgres:postgres@localhost:5432/Riddles"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)

from  project import routes