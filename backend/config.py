from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)   # to send back to front w/o error
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"     # to set up dabase
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
