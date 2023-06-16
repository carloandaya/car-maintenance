from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///car-maintenance.db"

db.init_app(app)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column("Make", db.String)
    model = db.Column("Model", db.String)

    def __repr__(self):
        return f"""<Car (Make: {self.make}, Model: {self.model})>"""
