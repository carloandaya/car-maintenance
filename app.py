from flask import render_template
from models import db, Car, app


@app.route("/")
def index():
    cars = Car.query.all()
    return render_template("index.html", cars=cars)


@app.route("/cars")
def cars():
    return render_template("cars.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")
