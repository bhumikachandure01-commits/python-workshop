import json


def save_students(students, filename):
    """Save students to a JSON file."""
    data = []

    for student in students:
        data.append(
            {
                "name": student.name,
                "age": student.age,
                "python": student.python,
                "mathematics": student.mathematics,
                "communication": student.communication,
            }
        )

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_students(filename, student_class):
    """Load students from a JSON file."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        students = []

        for item in data:
            student = student_class(
                item["name"],
                item["age"],
                item["python"],
                item["mathematics"],
                item["communication"],
            )
            students.append(student)

        return students

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []
