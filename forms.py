from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AddCarForm(FlaskForm): 
    year = StringField('Year', validators=[DataRequired()])
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    vin = StringField('VIN')