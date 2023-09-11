from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost:5432/parking"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret-key"

db = SQLAlchemy(app)

@app.route("/")
def index():
    from app.models import ParkingLot, Profit
    today = datetime.now().date()
    daily_profit = Profit.query.filter_by(date=today).first()
    if daily_profit:
        daily_profit = round(daily_profit.profit, 2)
    else:
        daily_profit = 0

    large_vehicles = ParkingLot.query.filter_by(id="2")
    medium_vehicles = ParkingLot.query.filter_by(id="1")
    small_vehicles = ParkingLot.query.filter_by(id="0")

    large_count = large_vehicles.first().available_space
    medium_count = medium_vehicles.first().available_space
    small_count = small_vehicles.first().available_space

    return render_template("index.html", large_count=large_count, medium_count=medium_count,
                           small_count=small_count, daily_profit=daily_profit)


from app.entry import vehicle_entry
from app.profit import profit
from app.exit import exit_vehicle
from app.capacity import capacity
