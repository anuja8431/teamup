from flask import Flask, render_template, request, redirect, session, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import json
from functools import wraps

app = Flask(__name__)
MAX_TEAMS = 1
app.secret_key = "secret"
CORS(app)

# Initialize with default admin user
users = [{
    "username": "admin",
    "password": "1234",
    "teams_joined": 0,
    "team_confirmed": False
}]

# # MongoDB connection
# # Replace with your MongoDB URI: mongodb+srv://<user>:<pass>@cluster.mongodb.net/teamup
# mongodb+srv://admin:admin123@cluster0.1mvod61.mongodb.net/?appName=cluster0
# client = MongoClient(MONGO_URI)
# db = client["teamup"]

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

# HOME
@app.route('/')
def home():
    return redirect('/login')


# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = {
            "username": request.form.get('username'),
            "password": request.form.get('password')
        }
        users.append(user)
        return redirect('/dashboard')

    return render_template('register.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        for user in users:
            if user['username'] == username and user['password'] == password:
                session["user"] = username
                return redirect('/dashboard')

        return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


# DASHBOARD
@app.route('/dashboard')
@login_required
def dashboard_page():
    return render_template('dashboard.html', current_page='dashboard')

@app.route('/settings')
@login_required
def settings_page():
    return render_template('settings.html', current_page='settings')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', current_page='profile')

@app.route('/brow')
@login_required
def browse():
    return render_template('brow.html', current_page='browse')

@app.route('/post')
@login_required
def posts():
    return render_template('post.html', current_page='post')

@app.route('/request')
@login_required
def requests_page():
    return render_template('request.html', current_page='request')


# RUN
if __name__ == '__main__':
    app.run(debug=True)

    