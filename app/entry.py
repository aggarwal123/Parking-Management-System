from app.main import app, db, index
from flask import render_template, request, flash, redirect, url_for
from app.models import Ticket, ParkingLot
from datetime import datetime


@app.route("/vehicle-entry", methods=["POST", "GET"])
def vehicle_entry():
    try:
        if request.method == "POST":
            number_plate = request.form["number_plate"].upper()
            category = request.form["category"]
            cate=0
            if category=="Small":
                cate=0
            elif category=="Medium":
                cate=1
            else:
                cate=2
            ticket = Ticket.query.filter_by(number_plate=number_plate).first()
            if ticket:
                flash("Vehicle Already in Parking")
                return render_template("entry.html")
            parking = ParkingLot.query.filter_by(id=cate).first()
            if parking.available_space > 0:
                parking.available_space -= 1
                entry_time = datetime.now()
                ticket = Ticket(number_plate=number_plate, category=cate, entry_time=entry_time)
                db.session.add(ticket)
                db.session.commit()
                return render_template("entry_ticket.html", ticket=ticket.id, number_plate=number_plate, category=category,
                                       entry_time=entry_time.time().strftime("%H:%M:%S"), entry_date=entry_time.date())
            else:
                flash(f"No Space Available for {category} category")
                return render_template("entry.html")
        else:
            return render_template("entry.html")
    except Exception as e:
        return f"<p>{str(e)}</p>"