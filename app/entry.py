from app.main import app, db, index
from flask import render_template, request, flash, redirect, url_for
from app.models import Vehicle, Ticket, ParkingLot
from datetime import datetime


@app.route("/vehicle-entry", methods=["POST", "GET"])
def vehicle_entry():
    try:
        if request.method == "POST":
            number_plate = request.form["number_plate"].upper()
            category = request.form["category"]
            if category=="small":
                category=0
            elif category=="medium":
                category=1
            else:
                category=2
            ticket = Ticket.query.filter_by(number_plate=number_plate).first()
            if ticket:
                flash("Vehicle Already in Parking")
                return render_template("entry.html")
            parking = ParkingLot.query.filter_by(id=category).first()
            if parking.available_space > 0:
                vehicle = Vehicle.query.filter_by(number_plate=number_plate).first()
                parking.available_space -= 1
                if not vehicle:
                    vehicle = Vehicle(number_plate=number_plate, category=category)
                    db.session.add(vehicle)
                entry_time = datetime.now()
                ticket = Ticket(number_plate=number_plate, category=category, entry_time=entry_time)
                db.session.add(ticket)
                db.session.commit()
                if category==0:
                    category="Small"
                elif category==1:
                    category="Medium"
                else:
                    category="Large"
                return render_template("entry_ticket.html", ticket=ticket.id, number_plate=number_plate, category=category,
                                       entry_time=entry_time.time().strftime("%H:%M:%S"), entry_date=entry_time.date())
            else:
                if category==0:
                    category="Small"
                elif category==1:
                    category="Medium"
                else:
                    category="Large"
                flash(f"No Space Available for {category} category")
                return render_template("entry.html")
        else:
            return render_template("entry.html")
    except Exception as e:
        return f"<p>{str(e)}</p>"