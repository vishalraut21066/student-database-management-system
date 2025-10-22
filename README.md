# Student Database Management System

A mini DBMS project for managing student records with CRUD operations using Python and SQLite.

## Description

This project implements a simple yet functional Database Management System for managing student information. It provides a command-line interface for performing Create, Read, Update, and Delete (CRUD) operations on student records.

## Features

- ✅ Add new student records
- ✅ View all students
- ✅ Update student information
- ✅ Delete student records
- ✅ Search students by ID
- ✅ SQLite database for persistent storage
- ✅ Clean and intuitive command-line interface

## Technologies Used

- **Python 3.x** - Programming language
- **SQLite3** - Database engine
- **Built-in Python libraries** - No external dependencies required

## Database Schema

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vishalraut21066/student-database-management-system.git
```

2. Navigate to the project directory:
```bash
cd student-database-management-system
```

3. No additional dependencies required! Python 3.x comes with SQLite3.

## Usage

Run the main program:
```bash
python student_dbms.py
```

### Menu Options:
1. **Add Student** - Enter student details (name, age, grade, email)
2. **View All Students** - Display all student records in the database
3. **Update Student** - Modify existing student information by ID
4. **Delete Student** - Remove a student record by ID
5. **Search Student** - Find a student by their ID
6. **Exit** - Close the application

## Project Structure

```
student-database-management-system/
│
├── student_dbms.py       # Main application file
├── database.db           # SQLite database (auto-generated)
├── README.md            # Project documentation
└── .gitignore          # Git ignore file
```

## Example Usage

```python
# Example of adding a student
Name: John Doe
Age: 20
Grade: A
Email: john.doe@example.com

# Student added successfully with ID: 1
```

## Future Enhancements

- [ ] Add GUI using Tkinter or PyQt
- [ ] Implement data validation
- [ ] Add export to CSV/Excel functionality
- [ ] Include student enrollment date
- [ ] Add authentication system
- [ ] Implement advanced search filters

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

## License

This project is open source and available for educational purposes.

## Contact

Created by [@vishalraut21066](https://github.com/vishalraut21066)

---
⭐ Star this repo if you find it helpful!
