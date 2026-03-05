import mysql.connector as db

# connect database
con = db.connect(user="root", password="Renuka@0414", host="localhost", database="students_db")

# create cursor object
cur = con.cursor()

# Create the students table 
cur.execute("""
    create table if not exists students_db (
        student_id varchar(255) primary key,
        name varchar(255),
        age int,
        grade varchar(1),
        contact_number varchar(10)
    )
""")

# Adds a new student to the database
def add_student():
    student_id = input("Enter student ID: ")
    query = "Select * from students_db where student_id = %s"
    cur.execute(query, (student_id,))
    student = cur.fetchone()
    if student:
        print()
        print("*"*23)
        print("Student already exists!")
        print("*"*23)
        print()
    else:
        name = input("Enter student name: ")
        name = name.capitalize()
        age = int(input("Enter student age: "))
        while age <= 0:
            print("Age should be greater than 0.")
            age = int(input("Enter student age: "))
        grade = input("Enter student grade (A-F): ").upper()
        while grade not in ['A', 'B', 'C', 'D', 'E', 'F']:
            print("Grade should be between A and F.")
            grade = input("Enter student grade (A-F): ").upper()
        contact_number = input("Enter contact number: ")
        while len(contact_number) != 10 or not contact_number.isdigit():
            print("Contact number should be 10 digits.")
            contact_number = input("Enter contact number: ")
        query = "Insert into students_db (student_id, name, age, grade, contact_number) values (%s, %s, %s, %s, %s)"
        cur.execute(query, (student_id, name, age, grade, contact_number))
        con.commit()
        print()
        print("Student added successfully!")
        print("-"*27)
        print()

# View student details
def view_students():
    query = "Select * from students_db"
    cur.execute(query)
    students = cur.fetchall()
    if students:
        for student in students:
            print(f"Student ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}, Contact Number: {student[4]}")
            print()
    else:
        print()
        print("No students found!")
        print("-"*18)
        print()
        
# update student informaton
def update_student():
    student_id = input("Enter student ID to update: ")
    query = "select * from students_db where student_id = %s"
    cur.execute(query, (student_id,))
    student = cur.fetchone()
    if student:
        name = input("Enter new student name: ")
        name = name.capitalize()
        age = int(input("Enter new student age: "))
        while age <= 0:
            print("Age should be greater than 0.")
            age = int(input("Enter new student age: "))
        grade = input("Enter new student grade (A-F): ").upper()
        while grade not in ['A', 'B', 'C', 'D', 'E', 'F']:
            print("Grade should be between A and F.")
            grade = input("Enter new student grade (A-F): ").upper()
        contact_number = input("Enter new contact number: ")
        while len(contact_number) != 10 or not contact_number.isdigit():
            print("Contact number should be 10 digits.")
            contact_number = input("Enter new contact number: ")
        query = "update students_db set name = %s, age = %s, grade = %s, contact_number = %s where student_id = %s"
        cur.execute(query, (name, age, grade, contact_number, student_id))
        con.commit()
        print()
        print("*"*29)
        print("Student updated successfully!")
        print("*"*29)
        print()
    else:
        print()
        print("Student not found!")
        print("-"*18)
        print()

# delete student records
def delete_student():
    student_id = input("Enter student ID to delete: ")
    query = "Select * from  students_db where student_id = %s"
    cur.execute(query, (student_id,))
    student = cur.fetchone()
    if student:
        query = "delete from students_db where student_id = %s"
        cur.execute(query, (student_id,))
        con.commit()
        print()
        print("-"*29)
        print("Student deleted successfully!")
        print("-"*29)
        print()
    else:
        print()
        print("Student not found!")
        print("-"*18)
        print()

# search student details
def search_student():
    student_id = input("Enter student ID to search: ")
    query = "Select * from students_db where student_id = %s"
    cur.execute(query, (student_id,))
    student = cur.fetchone()
    if student:
        print()
        print(f"Student ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}, Contact Number: {student[4]}")
        print()
    else:
        print()
        print("Student not found!")
        print("-"*18)
        print()

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        search_student()
    elif choice == 6:
        break
    else:
        print("Invalid choice!")

# close cursor
cur.close()
# close connection
con.close()
