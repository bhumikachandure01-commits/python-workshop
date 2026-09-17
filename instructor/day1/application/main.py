from student import Student
from student_manager import StudentManager
from storage import load_students, save_students


manager = StudentManager()

manager.students = load_students("students.json", Student)


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Find Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        python = float(input("Enter marks for Python: "))
        mathematics = float(input("Enter marks for Mathematics: "))
        communication = float(input("Enter marks for Communication: "))

        student = Student(name, age, python, mathematics, communication)

        manager.add_student(student)
        print("Student added successfully.")

        save_students(manager.students, "students.json")

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        name = input("Enter student name: ")
        student = manager.find_student(name)

        if student:
            student.display()
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name to update: ")

        python = float(input("Enter new marks for Python: "))
        mathematics = float(input("Enter new marks for Mathematics: "))
        communication = float(input("Enter new marks for Communication: "))

        updated = manager.update_student(name, python, mathematics, communication)

        if updated:
            save_students(manager.students, "students.json")
            print("Student updated successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        name = input("Enter student name to delete: ")

        deleted = manager.delete_student(name)

        if deleted:
            save_students(manager.students, "students.json")
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Exiting application.")
        break

    else:
        print("Invalid choice.")
