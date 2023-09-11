from flask import render_template, flash, request
from app.main import app, db
from app.models import Ticket, ParkingLot, Profit
from datetime import datetime


def price_calculation(category, entry_time, exit_time):
    if exit_time is None:
        return None
    duration = exit_time - entry_time
    duration = duration.total_seconds() / 3600
    price=0
    # FIXED PRICE OF 3 HRS
    if category==0:
        price = 90
    elif category==1:
        price = 180
    elif category==2:
        price = 300
    # CALCULATING PRICE AFTER 3 HRS
    if duration>3:
        if category==0:
            price += 20 * (duration-3)
        if category==1:
            price += 45 * (duration-3)
        if category==2:
            price += 75 * (duration-3)
    return (price, duration)


@app.route("/exit-vehicle", methods=["POST", "GET"])
def exit_vehicle():
    try:
        if request.method == "POST":
            ticket_id = request.form["ticket_id"]
            ticket = Ticket.query.filter(Ticket.id==ticket_id).first() # GETTING TICKET FROM THE DATABASE
            if ticket:
                id = ticket.id
                exit_time = datetime.now()
                exit_date = exit_time.date()
                entry_time = ticket.entry_time
                entry_date = entry_time.date()
                number_plate = ticket.number_plate
                category = ticket.category
                price, duration = price_calculation(category, ticket.entry_time, exit_time)
                total_time = f"{int(duration)} Hrs and {round((duration-int(duration))*60, 2)} mins"
                # UPDATING SPACE AVAILABLE
                parking = ParkingLot.query.filter_by(id=category).first()
                parking.available_space += 1
                # UPDATING THE PROFIT PER DAY
                date_profit = Profit.query.filter_by(date=exit_date).first()
                if date_profit:
                    date_profit.profit += price
                else:
                    date_profit = Profit(date=exit_date, profit=price)
                    db.session.add(date_profit)
                db.session.delete(ticket)
                db.session.commit()
                if category==0:
                    category="Small"
                elif category==1:
                    category="Medium"
                else:
                    category="Large"
                price=f"INR {round(price, 2)}"
                return render_template("exit_ticket.html", ticket=id, entry_time=entry_time.time().strftime("%H:%M:%S"), exit_time=exit_time.time().strftime("%H:%M:%S"),
                                    duration=total_time, cost=price, number_plate=number_plate, category=category,
                                    entry_date=entry_date, exit_date=exit_date)
            else:
                flash("Ticket Id Not Available")
                return render_template("exit.html")
        else:
            return render_template("exit.html")
    except Exception as e:
        return f"<h1>{str(e)}</h1>"