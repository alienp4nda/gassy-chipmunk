from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

seed_vehicles = [
    {"id": "1", "name": "VroomVroom", "year": 2010, "make": "Nissan", "model": "Moco", "milage": 123456},
    {"id": "2", "name": "ZoomZoom", "year": 2000, "make": "Mazda", "model": "LaPuta", "milage": 12345},
]


@app.route("/")
def main():
    return render_template("index.html", vehicles=seed_vehicles)


@app.route("/vehicle/<id>/fillup")
def fillup(id=None):
    # vehicle = filter(lambda x: x['id'] == id, seed_vehicles)
    vehicle = next((x for x in seed_vehicles if x['id'] == id), None)
    if vehicle is None:
        return redirect('/')
    return render_template("fillup.html", vehicle=vehicle)


@app.route("/vehicle/add", methods=["POST"])
def add_vehicle():
    vehicle = {
        "id": len(seed_vehicles) + 1,
        "name": request.form["name"],
        "make": request.form["make"],
        "year": request.form["year"],
        "model": request.form["model"],
        "milage": request.form["milage"],
    }
    seed_vehicles.append(vehicle)
    return render_template("vehicle.html", vehicle=vehicle, form_submitted = True)

@app.route("/vehicle/form", methods=["GET"])
def vehicle_form():
    return render_template('add_vehicle_form.html')
