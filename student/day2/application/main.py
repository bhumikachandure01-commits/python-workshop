from student import Student
from student_manager import StudentManager
from storage import load_students, save_students
from student_api import get_user_details


manager = StudentManager()

# TODO: Load students from students.json


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
        # TODO: Read student details
        # TODO: Create a Student object
        # TODO: Add the student
        # TODO: Save students
        pass

    elif choice == "2":
        # TODO: View students
        pass

    elif choice == "3":
        # TODO: Read student name
        # TODO: Find the student

        # TODO: If the student is found:
        #       - Display the student
        #       - Call get_user_details()
        #       - Display additional API information
        pass

    elif choice == "4":
        # TODO: Read student name and new marks
        # TODO: Update the student
        # TODO: Save students
        pass

    elif choice == "5":
        # TODO: Read student name
        # TODO: Delete the student
        # TODO: Save students
        pass

    elif choice == "6":
        print("Exiting application.")
        break

    else:
        print("Invalid choice.")
