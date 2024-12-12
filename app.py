from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "subhAM123$%"  # Replace with environment variable in production

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="flask_app",
    password="12345678",
    database="resume_builder"
)
cursor = db.cursor()

# Home page
@app.route('/')
def index():
    return render_template("index.html")

# Total job solution page
@app.route('/total_job_solution')
def total_job_solution():
    return render_template("total_job_solution.html")

# Resume sample or tutorial
@app.route('/user/resume_sample', methods=['GET'])
def resume_sample():
    return render_template('resume_sample.html')  

# Sign up page
@app.route('/user/signup_page', methods=['GET'])
def signup_page():
    return render_template('signup.html')

# Sign up methods
@app.route('/user/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
   
    hashed_password = generate_password_hash(password)

    insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, email, hashed_password))
    db.commit()

    # Save user info in session
    session['name'] = name
    session['email'] = email

    # Redirect to dashboard
    return render_template('index.html', data={"name": name})

# Login page    
@app.route('/user/login_page', methods=['GET'])
def login_page():
    return render_template('login.html')

# Login methods
@app.route('/user/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    query = "SELECT id, name, password FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    row = cursor.fetchone()

    if row and check_password_hash(row[2], password):
        # Save user info in session
        session["id"] = row[0]
        session["name"] = row[1]
        session["email"] = email

        flash("Login successful")
        return render_template("index.html", data={"user_id": row[0], "name": row[1]})
    else:
        flash("Invalid email or password")
        return redirect(url_for('login_page'))

# Dashboard page
@app.route('/user/dashboard', methods=['GET'])
def dashboard():
    if 'name' in session:
        user_name = session['name']
        return render_template("dashboard.html", name=user_name)
    else:
        flash("Please log in to access the dashboard.")
        return redirect(url_for('login_page'))

@app.route('/template1', methods=['GET'])
def resume_tamplate1():
    return render_template("template_1.html")

@app.route('/template2', methods=['GET'])
def resume_tamplate2():
    return render_template("template_2.html")

@app.route('/template3', methods=['GET'])
def resume_tamplate3():
    return render_template("template_3.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
