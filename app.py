from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (replace with MongoDB later)
users = []

# ================= HOME =================
@app.route('/')
def home():
    return redirect('/register')


# ================= REGISTER PAGE =================
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        # Step 1 data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Save basic data temporarily
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password
        }

        users.append(user)

        print("User Registered:", user)

        return redirect('/dashboard')

    return render_template('register.html')


# ================= PROFILE STEP =================
@app.route('/register/profile', methods=['POST'])
def register_profile():

    job_title = request.form.get('job_title')
    role = request.form.get('role')
    timezone = request.form.get('timezone')
    phone = request.form.get('phone')
    bio = request.form.get('bio')

    profile = {
        "job_title": job_title,
        "role": role,
        "timezone": timezone,
        "phone": phone,
        "bio": bio
    }

    print("Profile Data:", profile)

    return redirect('/dashboard')


# ================= LOGIN =================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect('/dashboard')

        return "Invalid Credentials ❌"

    return render_template('login.html')


# ================= DASHBOARD =================
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)