from flask import Flask
from flask import render_template

app = Flask(__name__)

seed_vehicles = [
    {"id": 1, "name": "VroomVroom", "year": 2010, "make": "Nissan", "model": "Moco"}
]

@app.route('/')
def main(vehicles=[]):
    return render_template('index.html', vehicles=seed_vehicles)

@app.route('/vehicle/<id>/fillup')
def fillup(id=None):
    return render_template('fillup.html', vehicle=seed_vehicles[0])