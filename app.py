from flask import render_template, request, redirect, url_for
from models import db, Car, app, Maintenance, MaintenanceType


@app.route("/")
def index():
    cars = Car.query.all()
    return render_template("index.html", cars=cars)


@app.route("/add-car", methods=["GET", "POST"])
def add_car():
    if request.form:
        car = Car(
            year=request.form["year"],
            make=request.form["make"],
            model=request.form["model"],
            vin=request.form["vin"],
        )
        db.session.add(car)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("addcar.html")


@app.route("/car/<id>")
def car(id):
    car = Car.query.filter_by(id=id).first()
    return render_template("car.html", car=car)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=8000, host="127.0.0.1")
