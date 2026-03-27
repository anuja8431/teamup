from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

users = []

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

        return "Invalid Credentials ❌"

    return render_template('login.html')


# DASHBOARD
@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

@app.route('/settings')
def settings_page():
    return render_template('settings.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/brow')
def browse():
    return render_template('brow.html')

@app.route('/post')
def posts():
    return render_template('post.html')

@app.route('/request')
def requests_page():
    return render_template('request.html')


# RUN
if __name__ == '__main__':
    app.run(debug=True)