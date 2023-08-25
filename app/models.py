from app.main import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_plate = db.Column(db.String(15), nullable=False, unique=True)
    category = db.Column(db.String(20), nullable=False)
    tickets = db.relationship('Ticket', backref='vehicle', lazy=True)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_plate = db.Column(db.String(15), db.ForeignKey('vehicle.number_plate'), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    entry_time = db.Column(db.DateTime, nullable=False)

class ParkingLot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parking_level = db.Column(db.String(50), nullable=False)
    total_capacity = db.Column(db.Integer, nullable=False)
    available_space = db.Column(db.Integer, nullable=False)

class Profit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    profit = db.Column(db.Float, nullable=False)

