from app.main import db

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_plate = db.Column(db.String(15), nullable=False)
    category = db.Column(db.Integer, nullable=False)
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

