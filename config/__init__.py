from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

DEV_DB = 'postgresql://insouser:postgres@localhost/DisasterAid'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB
db = SQLAlchemy(app)
CORS(app)
