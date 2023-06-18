from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///car-maintenance.db"

db.init_app(app)


class Car(db.Model):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    year = Column("Year", Integer)
    make = Column("Make", String)
    model = Column("Model", String)
    vin = Column("VIN", String)
    maintenance = relationship("Maintenance", back_populates="car")

    def __repr__(self):
        return f"""<Car (Year: {self.year}, Make: {self.make}, Model: {self.model}, VIN: {self.vin})>"""
    

class Maintenance(db.Model): 
    __tablename__ = "maintenance"

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey("cars.id"))
    car = relationship("Car", back_populates="maintenance")
