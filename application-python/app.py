from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Update the database URI with the new GCP PostgreSQL details
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://airline_booking:kl27b9193@34.41.51.77:5432/booking-website'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(50), nullable=False)
    departure_city = db.Column(db.String(100), nullable=False)
    arrival_city = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departure_city = db.Column(db.String(100), nullable=False)
    arrival_city = db.Column(db.String(100), nullable=False)
    departure_date = db.Column(db.String(100), nullable=False)
    return_date = db.Column(db.String(100))
    passengers = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_flight():
    departure_city = request.form.get('departure')
    arrival_city = request.form.get('arrival')
    departure_date = request.form.get('departure_date')
    return_date = request.form.get('return_date')
    passengers = request.form.get('passengers')
    
    new_booking = Booking(
        departure_city=departure_city,
        arrival_city=arrival_city,
        departure_date=departure_date,
        return_date=return_date,
        passengers=passengers
    )
    
    db.session.add(new_booking)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they do not exist
    app.run(host='0.0.0.0', port=5000)






