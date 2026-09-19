class StudentManager:
    """Manage a collection of students."""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        """Add a student to the collection."""
        self.students.append(student)

    def view_students(self):
        """Display all students."""
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display()

    def find_student(self, name):
        """Find a student by name."""
        for student in self.students:
            if student.name.lower() == name.lower():
                return student

        return None

    def update_student(
        self,
        name,
        python,
        mathematics,
        communication,
    ):
        """Update marks for an existing student."""
        student = self.find_student(name)

        if student is None:
            return False

        student.python = python
        student.mathematics = mathematics
        student.communication = communication

        return True

    def delete_student(self, name):
        """Delete a student by name."""
        student = self.find_student(name)

        if student is None:
            return False

        self.students.remove(student)
        return True
