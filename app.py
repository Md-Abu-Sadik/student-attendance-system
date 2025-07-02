from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# 🏗️ Initialize database (run once)
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    # Create students table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create attendance table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            status TEXT
        )
    ''')

    # Insert sample students (only if table is empty)
    students = cur.execute("SELECT * FROM students").fetchall()
    if not students:
        cur.execute("INSERT INTO students (name, phone_no) VALUES (?, ?)", ("Sadee", "01700000000"))
        cur.execute("INSERT INTO students (name, phone_no) VALUES (?, ?)", ("Tahriapi", "01700000001"))
        conn.execute("INSERT INTO students (name, phone_no) VALUES ('Ayesha', '01711111111')") 
        conn.execute("INSERT INTO students (name, phone_no) VALUES ('Riyad', '01722222222')")
        conn.execute("INSERT INTO students (name, phone_no) VALUES ('Imran', '01733333333')")
    conn.commit()
    conn.close()

# 🏠 Login page
@app.route('/')
def home():
    return render_template('login.html')

# 🔐 Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # ✅ Make sure these values match exactly
        if email == 'admin@example.com' and password == 'admin':
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid email or password"
            return render_template('login.html', error=error)

    return render_template('login.html')

# 📋 Dashboard - show students
@app.route('/dashboard', methods=['GET'])
def dashboard():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template('dashboard.html', students=students)

# ✅ Mark attendance
@app.route('/mark', methods=['POST'])
def mark_attendance():
    selected_students = request.form.getlist('students')
    date = request.form['date']
    conn = get_db_connection()
    cur = conn.cursor()

    for student_id in selected_students:
        cur.execute(
            "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
            (student_id, date, 'present')
        )

    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

    # Show the Add Student form
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')

        conn = get_db_connection()
        conn.execute("INSERT INTO students (name, phone_no) VALUES (?, ?)", (name, phone))
        conn.commit()
        conn.close()

        return redirect(url_for('dashboard'))  # Go back to dashboard after adding

    return render_template('add_student.html')


# 🚀 Run the app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
