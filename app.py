import json
import os
import random
import string
import requests
from flask import Flask, redirect, render_template, session, url_for, request, flash, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

from models import db, connect_db, Patient, User
from forms import NewPatientForm, PatientEditForm

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

AUTH_URL = 'https://accounts.google.com/o/oauth2/auth'

app.app_context().push()
connect_db(app)
db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

oauth = OAuth(app)

client_id=os.environ.get('GOOGLE_CLIENT_ID'),
client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),


oauth.register(
    name='google',
    client_id=os.environ.get('GOOGLE_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    },
    redirect_uri='https://schedule-app6.onrender.com/signin-google'
)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    """Display sign-in page."""
    return render_template('signin.html', session=session.get("user"), pretty=json.dumps(session.get("user"), indent=4))

def generate_nonce(length=16):
    #Generate a random nonce.
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@app.route('/google-login')
def google_login():
    """Initiate Google OAuth login."""
    nonce = generate_nonce()
    session['nonce'] = nonce
    print(f"Generated nonce: {nonce}")
    redirect_uri = url_for('google_callback', _external=True)
    return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)

@app.route('/signin-google')
def google_callback():
    """Handles OAuth callback and user login."""
    token = oauth.google.authorize_access_token()
    nonce = session.pop('nonce', None)
    
    if nonce is None:
        return 'Missing nonce in session', 400
    user_info = oauth.google.parse_id_token(token, nonce=nonce)
    session['user'] = user_info
   
    # Logic to handle user login or registration
    user = User.query.filter_by(email=user_info['email']).first()
    if user is None:
        user = User(
            email=user_info['email'], 
            name=user_info['name']
            )
        db.session.add(user)
        db.session.commit()
    login_user(user)
    return redirect('/calendar')

@app.route('/logout')
def logout():
    """Logs out the current user."""
    session.pop('user', None)
    logout_user()
    return redirect(url_for('home'))


@app.route('/calendar', methods=["GET"])
@login_required
def show_cal():
    """Display the calendar. Protected route."""
    return render_template('homepage.html')

@app.route('/pt-list', methods=["GET"])
@login_required
def show_pt_list():
    """Displays the list of patients. Protected route."""
    patients = Patient.query.all()
    return render_template('pt-list.html', patients=patients)

@app.route('/add-pt', methods=["GET", "POST"])
@login_required
def add_pt_form():
    """Handles adding a new patient. Protected route."""
    form = NewPatientForm()
    if form.validate_on_submit():
        new_patient = Patient(
            name=form.name.data,
            address=form.address.data,
            city=form.city.data,
            frequency=form.frequency.data,
            timeframe_start=form.timeframe_start.data,
            timeframe_end=form.timeframe_end.data
        )
        db.session.add(new_patient)
        db.session.commit()
        return redirect('/pt-list')
    return render_template("add-pt.html", form=form)

@app.route('/edit-pt/<int:patient_id>', methods=["GET", "POST"])
@login_required
def edit_pt_form(patient_id):
    """Handles editing a specific patient. Protected route."""
    patient = Patient.query.get(patient_id)
    if not patient:
        abort(404)
    form = PatientEditForm(obj=patient)
    if form.validate_on_submit():
        form.populate_obj(patient)
        db.session.commit()
        return redirect("/pt-list")
    return render_template("edit-pt.html", form=form, patient=patient)

@app.route('/pt-list/<int:patient_id>/delete', methods=["DELETE"])
@login_required
def delete_pt(patient_id):
    """Handles deleting a specific patient. Protected route."""
    patient = Patient.query.get(patient_id)
    if not patient:
        abort(404)
    try:
        db.session.delete(patient)
        db.session.commit()
        flash(f"{patient.name} has been deleted successfully.")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting patient: {str(e)}", 'error')
    return redirect(url_for("show_pt_list"))

if __name__ == '__main__':
    app.run(debug=True)
