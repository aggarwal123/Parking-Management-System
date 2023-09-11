from app.main import app, db
from app.models import ParkingLot
from flask import render_template, request, flash

@app.route("/capacity", methods=["POST", "GET"])
def capacity():
    try:
        if request.method == "POST":
            category = request.form["category"]
            capacity = request.form["capacity"]
            available = request.form["available"]
            cate=0
            if category == "medium":
                cate=1
            elif category == "large":
                cate=2
            if available>capacity:
                flash("Available Capacity cannot exceed Total Capacity")
                return render_template("capacity.html")
            parking = ParkingLot.query.filter_by(id=cate).first()
            parking.total_capacity = capacity
            parking.available_space = available
            db.session.commit()
            flash(f"{category.capitalize()} vehicle capacity is changed")
            return render_template("capacity.html")
        else:
            return render_template("capacity.html")
    except Exception as e:
        return f"<p>{str(e)}</p>"