<<<<<<< HEAD
# Student Attendance Management System

A beginner-friendly web project to mark and view student attendance using basic HTML and Bootstrap.

## Tech Stack
- HTML5
- Bootstrap 5

## Pages Created
- `login.html`: Teacher login page
- `dashboard.html`: Page to mark attendance
- add_student : page to add student
  

## How to View
1. Open each `.html` file in your browser directly.
2. (Backend integration will be added on week 2)

## Folder Structure
=======
# Student Attendance Management System

A beginner-friendly web project to mark and view student attendance using basic HTML and Bootstrap.

## Tech Stack
- HTML5
- Bootstrap 5

## Pages Created
- `login.html`: Teacher login page
- `dashboard.html`: Page to mark attendance
- *add_students :page to add student
  

## How to View
1. Open each `.html` file in your browser directly.
2. (Backend integration will be added on week 2)

## Folder Structure

student-attendance-system/
├── templates/
│ ├── login.html
│ └── dashboard.html
├── static/css/
├── README.md
>>>>>>> 52508a365a712a55204b34c2af1df7df32f2f83a


# 📚 Week 2 – Student Attendance Management System (Backend Integration with Flask & SQLite)

## ✅ Summary
This week, we connected our front-end (HTML + Bootstrap) to the backend using **Flask** and **SQLite**. We created routes to handle login, display student lists dynamically from the database, and record attendance entries. We also added a new feature to allow adding students via a form.

---

## 🔧 Technologies Used

- **Python (Flask Framework)** – Backend server
- **SQLite** – Lightweight file-based database
- **HTML + Bootstrap** – Frontend structure and styling
- **Jinja2** – Templating engine for dynamic HTML rendering
- **DB Browser for SQLite** – Optional GUI for managing the database

---

## 📂 Folder Structure

student-attendance-system/
├── app.py
├── database.db
├── templates/
│ ├── login.html
│ ├── dashboard.html
│ └── add_student.html
├── static/
│ └── (Bootstrap CDN used — no files inside)
└── README.md


---

## ✅ Features Implemented in Week 2

### 1. 🔐 Dummy Login System
- Hardcoded email: `admin@example.com`
- Password: `admin`
- Redirects to dashboard on success, shows error on failure.

### 2. 📋 Student List from Database
- Students are fetched dynamically from the `students` table.
- Each student is listed with a checkbox to mark attendance.

### 3. 🗓️ Attendance Marking
- User selects a date and marks students as “Present”.
- Data is saved into the `attendance` table with:
  - `student_id`
  - `date`
  - `status = present`

### 4. ➕ Add Student Form
- Added button in dashboard to navigate to `/add_student`
- User can add a student name and phone number.
- New student is inserted into the database and shown on the dashboard.

---

## 📌 Database Tables

### `students`
| Column     | Type    | Notes        |
|------------|---------|--------------|
| id         | INTEGER | PRIMARY KEY  |
| name       | TEXT    | NOT NULL     |
| phone_no   | TEXT    | NOT NULL     |

### `attendance`
| Column      | Type    | Notes                 |
|-------------|---------|------------------------|
| id          | INTEGER | PRIMARY KEY           |
| student_id  | INTEGER | Foreign key to student|
| date        | TEXT    | Attendance date       |
| status      | TEXT    | present/absent        |

---

## 🧪 How to Test

1. Run the app:
   ```bash
   python app.py

2. Go to: http://localhost:5000/

3. Login using:

   Email: admin@example.com

   Password: admin

4. On dashboard:

   - View student list

   - Mark attendance

   - Add new students
