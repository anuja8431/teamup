from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------- DB CONNECT ----------
def get_db():
    return sqlite3.connect("database.db")

# LOGIN PAGE
@app.route('/')
def login_page():
    return render_template("login.html")

# LOGIN
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # SAME logic (no change)
    if username == "admin" and password == "1234":
        return redirect('/dashboard')
    else:
        return "Invalid"

# DASHBOARD
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

# CREATE PAGE
@app.route('/create')
def create_post():
    return render_template("create_post.html")

# ✅ ADD POST (NOW CONNECTED)
@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']

    db = get_db()
    db.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    db.commit()

    return redirect('/posts')

# ✅ SHOW POSTS (NOW CONNECTED)
@app.route('/posts')
def posts():
    db = get_db()
    all_posts = db.execute("SELECT * FROM posts").fetchall()
    return render_template("posts.html", posts=all_posts)

app.run(debug=True)