"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, RaspSensor
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

@app.route('/sensor/<string:sensor_name>', methods=['POST'])
def add_data(sensor_name):  
    body = request.get_json()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'sensor_name' not in body:
        raise APIException('You need to specify the name room', status_code=400)
    if 'temperature_measure' not in body:
        raise APIException('You need to specify the temperature measure', status_code=400)
    if 'humidity_measure' not in body:
        raise APIException('You need to specify the humidity measure', status_code=400)

    new_data = RaspSensorm(sensor_name = body['sensor_name'], temperature_measure = body["temperature_measure"], humidity_measure = body["humidity_measure"])
    new_data.create()

    return jsonify({'status': 'OK', 'message': 'New Data posted succesfully'}), 201

@app.route('/sensor/<string:sensor_name>', methods=['GET'])
def get_rooms(sensor_name):
    sensor = RaspSensorm.read_by_sensor(sensor_name)
    if rooms is None:
        return "You need to specify the request sensor id as a json object, is empty", 400
    return jsonify(sensor), 200

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
