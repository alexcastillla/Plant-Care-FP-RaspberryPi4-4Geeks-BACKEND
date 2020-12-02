from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Boolean, Text, Float, Table, Date
from datetime import datetime

db = SQLAlchemy()

class RaspSensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_name = db.Column(db.String(255), unique=True, nullable=False)
    temperature_measure = db.Column(db.Float, unique=False, nullable=False)
    humidity_measure = db.Column(db.Float, unique=False, nullable=False)
    time_stamp = db.Column(db.Date, unique=False, nullable=False)

    def __repr__(self):
        return '<RaspSensor %r>' % self.sensor_name

    def serialize(self):
        return {
            "id": self.id,
            "sensor_name": self.sensor_name,
            "temperature_sensor": self.temperature_sensor,
            "humidity_sensor": self.humidity_sensor,
            "time_stamp": self.time_stamp,
        }

    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read_by_sensor(cls, sensor_id):
        sensor_by_user = RaspSensor.query.filter_by(sensor_name = sensor_name)
        sensor_from_user = list(map(lambda x: x.serialize(), sensor_by_user))
        return sensor_from_user

