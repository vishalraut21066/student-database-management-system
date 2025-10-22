"""
Flask Web Application for Student Database Management System
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'

DATABASE = 'database.db'

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Home page - Display all students"""
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=('GET', 'POST'))
def add_student():
    """Add new student"""
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        email = request.form['email']
        
        if not name or not age or not grade or not email:
            flash('All fields are required!', 'error')
        else:
            try:
                conn = get_db_connection()
                conn.execute('INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)',
                           (name, age, grade, email))
                conn.commit()
                conn.close()
                flash(f'Student {name} added successfully!', 'success')
                return redirect(url_for('index'))
            except sqlite3.IntegrityError:
                flash('Email already exists!', 'error')
    
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_student(id):
    """Edit student information"""
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    
    if student is None:
        conn.close()
        flash('Student not found!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        email = request.form['email']
        
        if not name or not age or not grade or not email:
            flash('All fields are required!', 'error')
        else:
            try:
                conn.execute('UPDATE students SET name = ?, age = ?, grade = ?, email = ? WHERE id = ?',
                           (name, age, grade, email, id))
                conn.commit()
                conn.close()
                flash(f'Student {name} updated successfully!', 'success')
                return redirect(url_for('index'))
            except sqlite3.IntegrityError:
                flash('Email already exists!', 'error')
    
    conn.close()
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>', methods=('POST',))
def delete_student(id):
    """Delete student"""
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    
    if student:
        conn.execute('DELETE FROM students WHERE id = ?', (id,))
        conn.commit()
        flash(f'Student {student["name"]} deleted successfully!', 'success')
    else:
        flash('Student not found!', 'error')
    
    conn.close()
    return redirect(url_for('index'))

@app.route('/search', methods=('GET', 'POST'))
def search_student():
    """Search for students"""
    students = []
    if request.method == 'POST':
        search_term = request.form['search_term']
        conn = get_db_connection()
        students = conn.execute(
            'SELECT * FROM students WHERE name LIKE ? OR email LIKE ? OR CAST(id AS TEXT) LIKE ?',
            (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%')
        ).fetchall()
        conn.close()
        
        if not students:
            flash(f'No students found matching "{search_term}"', 'info')
    
    return render_template('search.html', students=students)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
