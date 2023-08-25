from app.main import app, db
from app.models import Profit
from flask import Flask, render_template, request, flash

@app.route("/profit", methods=["GET", "POST"])
def profit():
    try:
        if request.method == "POST":
            date = request.form["date"]
            details = Profit.query.filter_by(date=date).first()
            if details:
                profit = round(details.profit, 2)
                flash(f"Profit : {profit}")
            else:
                flash("Data Not Found")
            return render_template("profit.html")
        return render_template("profit.html")
    except Exception as e:
        return f"<p>{str(e)}</p>"