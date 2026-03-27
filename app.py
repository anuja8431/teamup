from flask import Flask, request, jsonify
from flask_cors import CORS
from db import users_collection

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is running!"
    @app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    user = {
        "name": data.get("name"),
        "email": data.get("email"),
        "password": data.get("password"),
        "skills": data.get("skills", [])
    }

    users_collection.insert_one(user)

    return jsonify({"message": "User created successfully"})
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    user = users_collection.find_one({
        "email": data.get("email"),
        "password": data.get("password")
    })

    if user:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401