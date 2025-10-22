"""
Student Database Management System
A mini DBMS project using Python and SQLite
"""

import sqlite3
import sys

class StudentDBMS:
    def __init__(self, db_name="database.db"):
        """Initialize the database connection"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        """Create students table if it doesn't exist"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        self.conn.commit()
    
    def add_student(self):
        """Add a new student to the database"""
        print("\n=== Add New Student ===")
        try:
            name = input("Enter student name: ").strip()
            age = int(input("Enter student age: "))
            grade = input("Enter student grade (A/B/C/D/F): ").strip().upper()
            email = input("Enter student email: ").strip()
            
            if not name or not email:
                print("❌ Name and email cannot be empty!")
                return
            
            self.cursor.execute(
                "INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)",
                (name, age, grade, email)
            )
            self.conn.commit()
            print(f"✅ Student '{name}' added successfully with ID: {self.cursor.lastrowid}")
        except ValueError:
            print("❌ Invalid input! Age must be a number.")
        except sqlite3.IntegrityError:
            print("❌ Email already exists in the database!")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def view_all_students(self):
        """Display all students in the database"""
        print("\n=== All Students ===")
        self.cursor.execute("SELECT * FROM students")
        students = self.cursor.fetchall()
        
        if not students:
            print("No students found in the database.")
            return
        
        print(f"\n{'ID':<5} {'Name':<20} {'Age':<5} {'Grade':<8} {'Email':<30}")
        print("-" * 70)
        for student in students:
            print(f"{student[0]:<5} {student[1]:<20} {student[2]:<5} {student[3]:<8} {student[4]:<30}")
    
    def update_student(self):
        """Update student information"""
        print("\n=== Update Student ===")
        try:
            student_id = int(input("Enter student ID to update: "))
            
            # Check if student exists
            self.cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
            student = self.cursor.fetchone()
            
            if not student:
                print(f"❌ No student found with ID: {student_id}")
                return
            
            print(f"\nCurrent details: {student[1]}, Age: {student[2]}, Grade: {student[3]}, Email: {student[4]}")
            print("\nEnter new details (press Enter to keep current value):")
            
            name = input(f"Name [{student[1]}]: ").strip() or student[1]
            age_input = input(f"Age [{student[2]}]: ").strip()
            age = int(age_input) if age_input else student[2]
            grade = input(f"Grade [{student[3]}]: ").strip().upper() or student[3]
            email = input(f"Email [{student[4]}]: ").strip() or student[4]
            
            self.cursor.execute(
                "UPDATE students SET name=?, age=?, grade=?, email=? WHERE id=?",
                (name, age, grade, email, student_id)
            )
            self.conn.commit()
            print(f"✅ Student ID {student_id} updated successfully!")
        except ValueError:
            print("❌ Invalid input!")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def delete_student(self):
        """Delete a student from the database"""
        print("\n=== Delete Student ===")
        try:
            student_id = int(input("Enter student ID to delete: "))
            
            # Check if student exists
            self.cursor.execute("SELECT name FROM students WHERE id=?", (student_id,))
            student = self.cursor.fetchone()
            
            if not student:
                print(f"❌ No student found with ID: {student_id}")
                return
            
            confirm = input(f"Are you sure you want to delete '{student[0]}'? (yes/no): ").lower()
            if confirm == 'yes':
                self.cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
                self.conn.commit()
                print(f"✅ Student ID {student_id} deleted successfully!")
            else:
                print("❌ Deletion cancelled.")
        except ValueError:
            print("❌ Invalid input!")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def search_student(self):
        """Search for a student by ID"""
        print("\n=== Search Student ===")
        try:
            student_id = int(input("Enter student ID to search: "))
            self.cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
            student = self.cursor.fetchone()
            
            if student:
                print(f"\n{'ID':<5} {'Name':<20} {'Age':<5} {'Grade':<8} {'Email':<30}")
                print("-" * 70)
                print(f"{student[0]:<5} {student[1]:<20} {student[2]:<5} {student[3]:<8} {student[4]:<30}")
            else:
                print(f"❌ No student found with ID: {student_id}")
        except ValueError:
            print("❌ Invalid input!")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def close(self):
        """Close database connection"""
        self.conn.close()

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("  STUDENT DATABASE MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")
    print("="*50)

def main():
    """Main function to run the DBMS"""
    dbms = StudentDBMS()
    
    print("\n✨ Welcome to Student Database Management System ✨")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                dbms.add_student()
            elif choice == '2':
                dbms.view_all_students()
            elif choice == '3':
                dbms.update_student()
            elif choice == '4':
                dbms.delete_student()
            elif choice == '5':
                dbms.search_student()
            elif choice == '6':
                print("\n👋 Thank you for using Student DBMS. Goodbye!")
                dbms.close()
                sys.exit(0)
            else:
                print("❌ Invalid choice! Please enter a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!")
            dbms.close()
            sys.exit(0)
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
