from datetime import date, datetime
from flask import render_template, request, redirect, url_for
from forms import AddCarForm
from models import db, Car, app, Maintenance, MaintenanceType, Mileage
from waitress import serve


@app.route("/")
def index():
    cars = Car.query.all()
    return render_template("index.html", cars=cars)


@app.route("/add-car", methods=["GET", "POST"])
def add_car():
    form = AddCarForm()
    if form.validate_on_submit():
        car = Car(
            year=form.year.data,
            make=form.make.data,
            model=form.model.data,
            vin=form.vin.data,
        )
        db.session.add(car)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("addcar.html", form=form)


@app.route("/add-maintenance/<car_id>", methods=["GET", "POST"])
def add_maintenance(car_id):
    return render_template("addmaintenance.html")


@app.route("/maintenance-type")
def maintenance():
    pass


@app.route("/add-maintenance-type", methods=["GET", "POST"])
def add_maintenance_type():
    return render_template("addmaintenancetype.html")


@app.route("/add-mileage/<car_id>", methods=["GET", "POST"])
def add_mileage(car_id):
    if request.form:
        mileage_date = datetime.strptime(request.form["date"], "%Y-%m-%d")
        mileage = Mileage(
            car_id=car_id, mileage=request.form["mileage"], date=mileage_date
        )
        db.session.add(mileage)
        db.session.commit()
        return redirect(url_for("car", id=car_id))
    return render_template("addmileage.html", car_id=car_id)


@app.route("/car/<id>")
def car(id):
    car = Car.query.filter_by(id=id).first()
    return render_template("car.html", car=car)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not Car.query.all():
            car = Car(year="2004", make="Honda", model="Accord")
            db.session.add(car)
            maintenance_type = MaintenanceType(description="Brake Pads")
            db.session.add(maintenance_type)
            maintenance = Maintenance(
                car_id=1, type_id=1, date=date(2022, 10, 15), mileage=184500
            )
            db.session.add(maintenance)
            db.session.commit()

    # app.run(debug=True, port=8000, host="127.0.0.1")
    serve(app, host="0.0.0.0", port=8080)
