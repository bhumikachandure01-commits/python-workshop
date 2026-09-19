# Day 1 Instructor Delivery Guide

## Purpose

This guide is the instructor's delivery reference for Day 1 of the Python workshop.

The workshop is taught as one continuous development story:

> Each new concept is introduced because the previous approach has a limitation.

The Day 1 progression is:

**Functions → Modules → Exceptions → File & JSON Handling → OOP → Encapsulation → Inheritance → Application Design → Student Management System**

For each stage, the guide records the teaching objective, problem to introduce, live-coding approach, student exercise, and transition to the next concept.

---

# Stage 1 — Functions

**Approximate time: 15–20 minutes**

## Objective

Students should understand:

- why functions are useful
- how to define and call a function
- parameters and arguments
- returning a value
- reusing the same logic for multiple inputs

## Problem to introduce

Start with repeated logic:

```python
student1_total = 80 + 75 + 90
student1_percentage = student1_total / 3

student2_total = 70 + 85 + 80
student2_percentage = student2_total / 3
```

Ask:

> What happens when we have 100 students?

Let students identify the repetition.

## Key message

Do not present a function only as a way to avoid repetition.

Emphasize:

> **A function separates a piece of logic from the code that uses it.**

This idea becomes important later when the application is divided into classes and modules.

## Live coding

Introduce:

```python
def calculate_percentage(python, mathematics, communication):
    total = python + mathematics + communication
    return total / 3
```

Then call it:

```python
percentage = calculate_percentage(80, 75, 90)

print("Percentage:", percentage)
```

Explain:

- `def` defines a function
- `calculate_percentage` is the function name
- parameters receive input
- `return` sends a result back to the caller

Demonstrate reuse:

```python
student1 = calculate_percentage(80, 75, 90)
student2 = calculate_percentage(70, 85, 80)

print(student1)
print(student2)
```

## Student exercise

Give students:

```python
def calculate_total(python, mathematics, communication):
    # Complete this function
    pass
```

Ask them to:

1. calculate the total
2. return the total
3. call the function for one student
4. print the result

Expected solution:

```python
def calculate_total(python, mathematics, communication):
    return python + mathematics + communication


total = calculate_total(80, 75, 90)

print("Total:", total)
```

## Transition to Modules

Ask:

> Our function is useful. What if we have 20 such functions?

Show the idea of a growing `main.py`:

```text
main.py
├── calculate_percentage()
├── calculate_total()
├── find_student()
├── validate_marks()
├── save_student()
└── load_student()
```

Ask:

> Should all of these functions live in one file?

Use the answer to introduce **modules** as the next step in organizing related code.

---

## Instructor Notes

- Keep the example simple; do not introduce advanced function concepts yet.
- Do not introduce lambda functions, decorators, recursion, type hints, or functional programming.
- Keep the focus on reusable logic and separation of responsibility.
- The Student Management System will provide the context for later stages.

---

# Day 1 Narrative

At every stage, connect the new concept to a limitation of the previous stage:

| Stage | Limitation / Need | Concept |
|---|---|---|
| Functions | Repeated logic | Functions |
| Modules | Too much code in one file | Modules |
| Exceptions | Programs fail on invalid input | Exception handling |
| File handling | Data disappears when program ends | Files |
| JSON | Need structured persistent data | JSON |
| OOP | Data and behavior are becoming difficult to manage | Classes and objects |
| Encapsulation | Need controlled access to object data | Encapsulation |
| Inheritance | Related objects share common behavior | Inheritance |
| Application design | Need clear separation of responsibilities | Architecture |
| CRUD | Need to manage real records | Student Management System |

This table is the overall teaching spine for Day 1.


# Stage 2 — Modules

**Approximate time: 15–20 minutes**

## Objective

Students should understand:

- why a program should be divided into multiple files
- what a Python module is
- how to define functions in one module
- how to import and use those functions from another file
- why modules improve organization and maintainability

## Connect from Stage 1

Start from the function created in Stage 1:

```python
def calculate_percentage(python, mathematics, communication):
    total = python + mathematics + communication
    return total / 3
```

Ask:

> We now have reusable functions. What happens when our application has many functions?

Show a growing single file:

```text
main.py
├── calculate_total()
├── calculate_percentage()
├── find_student()
├── validate_marks()
├── save_student()
├── load_student()
└── display_student()
```

Ask:

> Is it a good idea to keep every piece of functionality in one file?

Use the students' answers to introduce the idea of **modules**.

## Key message

Emphasize:

> **A module is a Python file that contains related code that can be reused by other Python files.**

The goal is not simply to create more files. The goal is to **organize related responsibilities**.

## Live coding

Create a module:

```text
student_utils.py
```

Move the reusable function into it:

```python
def calculate_percentage(python, mathematics, communication):
    total = python + mathematics + communication
    return total / 3
```

Then create:

```text
main.py
```

Import the function:

```python
from student_utils import calculate_percentage
```

Use it:

```python
percentage = calculate_percentage(80, 75, 90)

print("Percentage:", percentage)
```

Run the program and show that the function still works even though it is defined in another file.

## Explain the relationship

Show:

```text
main.py
    |
    | imports
    v
student_utils.py
    |
    └── calculate_percentage()
```

Explain:

- `student_utils.py` is the module
- `calculate_percentage()` belongs to that module
- `main.py` uses the function by importing it
- the code is now separated by responsibility

## Demonstrate multiple functions

Add another related function:

```python
def calculate_total(python, mathematics, communication):
    return python + mathematics + communication
```

Then:

```python
from student_utils import calculate_percentage, calculate_total
```

Use both functions:

```python
total = calculate_total(80, 75, 90)
percentage = calculate_percentage(80, 75, 90)

print("Total:", total)
print("Percentage:", percentage)
```

This demonstrates why grouping related functions into a module is useful.

## Student exercise

Give students a small module exercise.

Create:

```text
marks_utils.py
```

Ask them to create:

```python
def calculate_total(python, mathematics, communication):
    # TODO: Return the total
    pass
```

Then in `main.py`:

```python
from marks_utils import calculate_total

total = calculate_total(80, 75, 90)

print("Total:", total)
```

Expected result:

```text
Total: 245
```

If time permits, ask them to add:

```python
def calculate_percentage(python, mathematics, communication):
    # TODO: Return the percentage
    pass
```

and import both functions.

## Important teaching point

Make the distinction clear:

```text
Function → organizes reusable logic

Module → organizes related functions/classes
```

This distinction will become important later when the application is split into:

```text
student.py
student_manager.py
storage.py
student_api.py
```

## Transition to Exceptions

Now deliberately create an input problem.

Instead of passing fixed numbers:

```python
python = float(input("Enter Python marks: "))
```

Ask the students:

> What happens if the user enters `abc`?

Let them run it and observe:

```text
ValueError
```

Ask:

> Our code is organized now, but what happens when the user gives invalid input?

This creates the need for the next concept:

> **Exception handling — allowing the program to handle errors instead of terminating unexpectedly.**

---

## Instructor Notes

- Do not introduce packages or `__init__.py` at this stage.
- Do not introduce advanced import mechanisms.
- Keep the distinction between a function and a module explicit.
- Avoid turning this into a Python packaging lesson.
- The later application structure will reinforce why modules are useful.
- The transition into exceptions should be demonstrated, not merely explained.

## Checkpoint

Before moving to Exceptions, students should be able to answer:

1. What is a function?
2. What is a module?
3. Why would we put related functions into a separate module?
4. How do we import a function from another Python file?


# Stage 3 — Exceptions

**Approximate time: 20–25 minutes**

## Objective

Students should understand:

- what an exception is
- why invalid input can cause a program to terminate
- how `try` and `except` work
- how to handle `ValueError`
- why exception handling should be placed around the operation that can fail
- how repeated validation logic can be moved into a reusable function

## Connect from Stage 2

Start with the modular program from the previous stage.

The code is now organized:

```text
main.py
    |
    | imports
    v
marks_utils.py
```

But organization does not prevent runtime errors.

Ask students to run:

```python
python = float(input("Enter marks for Python: "))
```

Enter:

```text
abc
```

The program produces:

```text
ValueError
```

Ask:

> The program is organized correctly. Why did it still fail?

Explain:

> **Modules organize our code. Exceptions help our program handle unexpected or invalid situations while it is running.**

## Key message

Emphasize:

> **An exception is an event that occurs during program execution that interrupts the normal flow of the program.**

For this workshop, focus on the practical case students are likely to encounter:

```text
User input
    ↓
float()
    ↓
Invalid value
    ↓
ValueError
```

Do not turn this into a taxonomy of every Python exception.

## Live coding — First observe the failure

Start with:

```python
marks_python = float(input("Enter marks for Python: "))
marks_math = float(input("Enter marks for Mathematics: "))
marks_comm = float(input("Enter marks for Communication: "))
```

Enter:

```text
85
abc
90
```

Point out:

- Python mark was accepted
- Mathematics input caused the failure
- execution stopped at that point
- Communication input was never reached

This makes the need for exception handling visible.

## Live coding — Introduce `try` / `except`

Wrap one input:

```python
try:
    marks_python = float(input("Enter marks for Python: "))
except ValueError:
    print("Invalid input. Please enter a number.")
```

Test with:

```text
85
```

and then:

```text
abc
```

Explain the flow:

```text
try
 ↓
Attempt operation
 ↓
Success ─────────→ continue
 ↓
ValueError
 ↓
except
 ↓
Handle the problem
```

## Demonstrate the limitation

Now show:

```python
try:
    marks_python = float(input("Enter marks for Python: "))
except ValueError:
    print("Invalid input. Please enter a number.")

marks_math = float(input("Enter marks for Mathematics: "))
marks_comm = float(input("Enter marks for Communication: "))
```

Enter `abc` for Python.

The error is handled, but the variable `marks_python` has not received a valid value.

If later code tries to use it, the program can still have a problem.

Ask:

> Should we simply print an error and continue, or should we ask the user for the value again?

This leads naturally to a validation loop.

## Live coding — Validate until the input is correct

Introduce:

```python
while True:
    try:
        marks_python = float(input("Enter marks for Python: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
```

Explain:

- `while True` keeps asking
- `try` attempts the conversion
- `ValueError` is caught
- invalid input causes another attempt
- `break` exits the loop after valid input

Test:

```text
abc
hello
85
```

The program should continue only after a valid number is entered.

## Important teaching point — Validate each input independently

Now show the three marks:

```python
while True:
    try:
        marks_python = float(input("Enter marks for Python: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        marks_math = float(input("Enter marks for Mathematics: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        marks_comm = float(input("Enter marks for Communication: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
```

Explain why each input has its own validation loop.

Suppose the user enters:

```text
Python: 85
Mathematics: 90
Communication: abc
```

We do **not** want to ask for Python and Mathematics again.

Only Communication should be requested again.

This is an important practical lesson:

> **Validate each independent input independently.**

## Live coding — Remove repetition with a function

The three loops are correct, but repetitive.

Ask:

> We learned functions earlier. Can we use a function here?

Introduce:

```python
def get_valid_mark(subject):
    """Get a valid numeric mark from the user."""
    while True:
        try:
            return float(input(f"Enter marks for {subject}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
```

Then:

```python
marks_python = get_valid_mark("Python")
marks_math = get_valid_mark("Mathematics")
marks_comm = get_valid_mark("Communication")
```

This is the key connection between the earlier stages:

```text
Functions
    ↓
Modules
    ↓
Exceptions
    ↓
Reusable validation function
```

The students now see that the concepts are not isolated topics.

## Student exercise

Give students the following:

```python
def get_valid_mark(subject):
    # TODO: Keep asking until the user enters a valid number
    pass


marks_python = get_valid_mark("Python")
marks_math = get_valid_mark("Mathematics")
marks_comm = get_valid_mark("Communication")
```

Ask them to:

1. use `while True`
2. read input
3. convert it to `float`
4. catch `ValueError`
5. print an error message
6. return the valid mark

Expected solution:

```python
def get_valid_mark(subject):
    """Get a valid numeric mark from the user."""
    while True:
        try:
            return float(input(f"Enter marks for {subject}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
```

## Business rule discussion

Briefly distinguish between:

**Technical input error**

```text
abc
```

This causes:

```python
ValueError
```

and can be handled with exception handling.

**Business rule**

```text
Marks must be between 0 and 100.
```

This is a validation rule.

For this workshop, demonstrate it simply:

```python
def get_valid_mark(subject):
    """Get a valid mark between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for {subject}: "))

            if 0 <= mark <= 100:
                return mark

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")
```

Do **not** introduce custom exceptions.

The important distinction is:

```text
Invalid data type → ValueError

Invalid business value → application validation
```

## Transition to File Handling

Now ask:

> We can safely accept the student's marks. What happens when the program ends?

Demonstrate:

```text
Start program
    ↓
Enter student data
    ↓
Calculate percentage
    ↓
Program exits
    ↓
Start again
    ↓
Student data is gone
```

Ask:

> How can we keep the data after the program ends?

This introduces the next stage:

> **File handling — storing data outside the running program.**

The progression is now:

```text
Functions
    ↓
Modules
    ↓
Exceptions
    ↓
File handling
```

## Instructor Notes

- Use `ValueError` as the main exception example.
- Let students see the unhandled exception before introducing `try/except`.
- Do not start with a large application example.
- Keep the first `try/except` deliberately small so students understand what is being protected.
- Demonstrate why simply printing an error is not enough.
- The validation loop is the important practical pattern.
- Reinforce that exceptions are not a replacement for ordinary business validation.
- Do not introduce custom exceptions, exception hierarchies, decorators, context managers, or advanced exception patterns.
- Keep `except` specific where possible; use `ValueError` here rather than a broad `except Exception`.

## Checkpoint

Before moving to File Handling, students should be able to answer:

1. What is an exception?
2. What happens when `float("abc")` is executed?
3. What is the purpose of `try`?
4. What is the purpose of `except`?
5. Why do we use a loop when validating user input?
6. Why should independent inputs have independent validation?
7. What is the difference between invalid input type and a business rule such as marks being between 0 and 100?


# Stage 4 — File & JSON Handling

**Approximate time: 25–30 minutes**

## Objective

Students should understand:

- why data needs to be persisted outside the running program
- how to open, read, and write a text file
- why `with open(...)` is preferred for file handling
- the difference between text data and structured data
- what JSON is and why it is useful for application data
- how to write Python data to JSON
- how to read JSON back into Python
- how file-related errors can be handled using exceptions

## Connect from Stage 3

Start from the validated student input.

The program can now safely accept:

```text
Student name
Python marks
Mathematics marks
Communication marks
```

Ask:

> What happens when we close the program?

Students should recognize that the values stored in variables disappear.

Show:

```text
Program starts
    ↓
Student enters data
    ↓
Data stored in variables
    ↓
Program exits
    ↓
Variables disappear
```

Ask:

> How can we keep the information after the program exits?

Introduce:

> **File handling allows a program to store and retrieve data outside the running program.**

## Key message

Emphasize:

> **Variables store data while the program is running. Files allow data to survive after the program ends.**

Do not begin with JSON. First demonstrate the basic idea using a simple text file.

---

## Part A — Basic File Handling

### Live coding — Write to a file

Start with:

```python
student_name = input("Enter student name: ")

with open("student.txt", "w") as file:
    file.write(student_name)

print("Student name saved successfully.")
```

Explain:

- `open()` opens or creates a file
- `"w"` means write mode
- `file.write()` writes data
- `with` manages the file safely
- the file is automatically closed when the block finishes

Run the program and inspect:

```text
student.txt
```

Show that the student's name is now physically stored in the file.

### Live coding — Read from a file

Add:

```python
with open("student.txt", "r") as file:
    name = file.read()

print("Student name:", name)
```

Explain:

- `"r"` means read mode
- `file.read()` reads the contents
- the result is returned as a Python string

Show the complete flow:

```text
Python program
      ↓
    write
      ↓
student.txt
      ↓
     read
      ↓
Python program
```

## Demonstrate persistence

Run the program.

Then stop it.

Start it again.

Explain:

> The Python variables disappeared when the program ended, but the file remained.

This is the first clear demonstration of **persistence**.

---

## Part B — Connect File Handling to the Student Data

Now move beyond just the name.

Create a Python dictionary:

```python
student = {
    "name": "Chetan",
    "python": 85,
    "mathematics": 78,
    "communication": 90
}
```

Ask:

> Can we simply use `file.write(student)`?

Explain that `file.write()` expects text, while `student` is a Python dictionary.

This creates the need for a structured data format.

---

# JSON

## Objective

Introduce JSON as the bridge between Python objects/data structures and stored application data.

## Key message

> **JSON is a text-based format commonly used to represent structured data.**

Show the Python dictionary:

```python
student = {
    "name": "Chetan",
    "python": 85,
    "mathematics": 78,
    "communication": 90
}
```

Then show the equivalent JSON:

```json
{
    "name": "Chetan",
    "python": 85,
    "mathematics": 78,
    "communication": 90
}
```

Point out that JSON looks very similar to a Python dictionary, but it is a data format rather than a Python object.

## Live coding — Save JSON

Introduce the `json` module:

```python
import json
```

Then:

```python
student = {
    "name": "Chetan",
    "python": 85,
    "mathematics": 78,
    "communication": 90
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student data saved successfully.")
```

Explain:

```text
Python dictionary
       ↓
   json.dump()
       ↓
    JSON file
```

Open `student.json` and show the students what was written.

The `indent=4` argument is useful because it makes the JSON human-readable.

## Live coding — Read JSON

Now load the data:

```python
with open("student.json", "r") as file:
    loaded_student = json.load(file)

print("Student data:")
print(loaded_student)
```

Explain:

```text
JSON file
    ↓
json.load()
    ↓
Python dictionary
```

Show that:

```python
print(loaded_student["name"])
print(loaded_student["python"])
```

works just like accessing the original dictionary.

---

## Part C — Multiple Students

Now introduce a list of dictionaries:

```python
students = [
    {
        "name": "Chetan",
        "python": 85,
        "mathematics": 78,
        "communication": 90
    },
    {
        "name": "Rahul",
        "python": 72,
        "mathematics": 88,
        "communication": 81
    }
]
```

Save it:

```python
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
```

Load it:

```python
with open("students.json", "r") as file:
    loaded_students = json.load(file)

for student in loaded_students:
    print(student)
```

This is an important bridge toward the Student Management System.

The students now see that application data can be represented as:

```text
List
  ↓
Dictionary
  ↓
JSON file
```

---

## Part D — File and JSON Exceptions

Connect directly back to Stage 3.

Ask:

> What happens if `students.json` does not exist?

Demonstrate:

```python
with open("students.json", "r") as file:
    loaded_students = json.load(file)
```

If the file does not exist:

```text
FileNotFoundError
```

Explain:

> We already learned how to handle exceptions. Now we are applying the same concept to file operations.

### Handle missing files

Introduce:

```python
import json


try:
    with open("students.json", "r") as file:
        loaded_students = json.load(file)

except FileNotFoundError:
    print("Student file not found.")
    loaded_students = []
```

Explain why an empty list is useful:

```text
No existing file
      ↓
Start with empty student collection
      ↓
Application can continue
```

### Handle invalid JSON

Deliberately corrupt the JSON file.

For example:

```json
{
    "name": "Chetan",
```

Then run the program.

Show:

```text
JSONDecodeError
```

Handle it:

```python
except json.JSONDecodeError:
    print("Invalid JSON data.")
    loaded_students = []
```

Now the complete loading pattern becomes:

```python
import json


try:
    with open("students.json", "r") as file:
        loaded_students = json.load(file)

except FileNotFoundError:
    print("Student file not found.")
    loaded_students = []

except json.JSONDecodeError:
    print("Invalid JSON data.")
    loaded_students = []
```

This reinforces the previous stage:

```text
Exceptions
    ↓
FileNotFoundError
JSONDecodeError
```

---

## Student Exercise

Give students a small persistence exercise.

Start with:

```python
students = [
    {
        "name": "Chetan",
        "python": 85,
        "mathematics": 78,
        "communication": 90
    }
]
```

Ask them to:

1. save the list to `students.json`
2. load it back
3. print the loaded students

Starter code:

```python
import json


students = [
    {
        "name": "Chetan",
        "python": 85,
        "mathematics": 78,
        "communication": 90
    }
]

# TODO: Save students to students.json


# TODO: Load students from students.json


# TODO: Display the loaded students
```

Expected solution:

```python
import json


students = [
    {
        "name": "Chetan",
        "python": 85,
        "mathematics": 78,
        "communication": 90
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    loaded_students = json.load(file)

print("Loaded students:")

for student in loaded_students:
    print(student)
```

If time permits, ask students to delete the file and observe what happens when they try to read it.

---

## Part E — Introduce a Storage Function

This is the bridge toward application architecture.

The code for saving and loading is useful, but we should not repeat it everywhere.

Ask:

> What if Add Student, Update Student, and Delete Student all need to save the data?

This creates another repetition problem.

Use the functions concept from Stage 1:

```python
import json


def save_students(students, filename):
    """Save student data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)


def load_students(filename):
    """Load student data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []

    except json.JSONDecodeError:
        print(f"Invalid JSON data in: {filename}")
        return []
```

Explain that we are beginning to build a reusable **storage responsibility**.

Do not yet turn this into the full `storage.py` application module. The complete separation will come during Application Design.

The conceptual progression is:

```text
File operations
      ↓
JSON
      ↓
Exception handling
      ↓
Reusable storage functions
      ↓
Storage module in the application
```

---

## Transition to OOP

At this point, the data looks like:

```python
student = {
    "name": "Chetan",
    "python": 85,
    "mathematics": 78,
    "communication": 90
}
```

Ask:

> We have the student's data. Where should the behavior related to that student live?

For example:

```text
Student data
    +
calculate percentage
    +
display student
    +
update marks
```

Ask:

> Would it be useful to represent a student as an object?

This introduces the next major concept:

> **Object-Oriented Programming — combining related data and behavior into objects.**

The progression becomes:

```text
Variables
    ↓
Functions
    ↓
Modules
    ↓
Exceptions
    ↓
Files
    ↓
JSON
    ↓
Objects
```

## Instructor Notes

- Start with a plain text file before introducing JSON.
- Make persistence visible by stopping and restarting the program.
- Do not start by saying "JSON is used by APIs." That connection belongs on Day 2.
- Show both `json.dump()` and `json.load()`.
- Make the Python ↔ JSON conversion explicit.
- Use a list of dictionaries because it closely matches the later Student Management System data.
- Demonstrate both `FileNotFoundError` and `JSONDecodeError`.
- Connect exception handling back to Stage 3 instead of presenting these as unrelated errors.
- Do not introduce databases, CSV libraries, serialization frameworks, or pandas.
- Keep the storage functions simple. The purpose here is to prepare students for the later `storage.py` module.
- Delete or clean up runtime-generated JSON files after the demonstration if the repository should remain clean.

## Checkpoint

Before moving to OOP, students should be able to answer:

1. Why do we need files?
2. What is persistence?
3. What does `with open(...)` do?
4. What is JSON?
5. What does `json.dump()` do?
6. What does `json.load()` do?
7. What happens if the JSON file does not exist?
8. What happens if the JSON content is invalid?
9. Why might saving/loading logic be placed into reusable functions?
10. Why might a dictionary become insufficient as the application grows?

## Day 1 Milestone

At the end of this stage, students have all the foundations needed to begin modeling the application:

```text
Functions
    → reusable logic

Modules
    → organized code

Exceptions
    → controlled failure

Files
    → persistence

JSON
    → structured persistence
```

The next step is to introduce a **Student object** that combines the student's data with behavior.


# Stage 5 — OOP: Classes & Objects

**Approximate time: 30–35 minutes**

## Objective

Students should understand:

- why dictionaries and separate functions become harder to manage as an application grows
- what a class is
- what an object is
- how to define a class
- how to create objects
- what `self` represents
- how `__init__` initializes object data
- how methods combine data and behavior
- how multiple objects can be created from the same class
- how a class provides a model for application entities

## Connect from Stage 4

At the end of the previous stage, the student data looks like:

```python
student = {
    "name": "Chetan",
    "age": 41,
    "python": 85,
    "mathematics": 78,
    "communication": 90
}
```

The application also has functions such as:

```python
calculate_percentage(...)
display_student(...)
```

Ask:

> What happens when we have 100 students?

We might end up with:

```text
student1 dictionary
student2 dictionary
student3 dictionary
...
student100 dictionary

calculate_percentage(student1)
calculate_percentage(student2)
...
display_student(student1)
display_student(student2)
...
```

Ask:

> The data belongs to a student. The behavior also belongs to a student. Can we model them together?

This introduces **Object-Oriented Programming**.

## Key message

Emphasize:

> **A class is a blueprint for creating objects. An object represents one instance of that class.**

For the workshop:

```text
Class
  ↓
Student

Objects
  ↓
student1
student2
student3
```

A useful analogy:

> A class is like a form/template describing what a student should have. Each filled-in form represents one student object.

Avoid spending too much time on abstract OOP terminology. Move quickly to code.

---

## Part A — Create the First Class

### Live coding — Empty class

Start with:

```python
class Student:
    pass
```

Explain:

- `class` defines a class
- `Student` is the class name
- `pass` means there is currently no implementation

Then create an object:

```python
student = Student()
```

Ask:

> What have we created?

Explain:

```text
Student
   ↓
class / blueprint

student
   ↓
object / instance
```

---

## Part B — Add Attributes

Show that an object can contain data:

```python
student = Student()

student.name = "Chetan"
student.age = 41
student.python = 85
```

Then:

```python
print(student.name)
print(student.age)
print(student.python)
```

Explain that these are **attributes** of the object.

Ask:

> If we create another student, do we want to manually assign every attribute again?

Demonstrate:

```python
student1 = Student()
student1.name = "Chetan"
student1.age = 41

student2 = Student()
student2.name = "Rahul"
student2.age = 21
```

This works, but it is repetitive.

Ask:

> Can the class initialize the object for us?

This introduces `__init__`.

---

# Part C — The `__init__` Method

## Live coding

Replace the class with:

```python
class Student:
    """Represent a student."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Create an object:

```python
student = Student("Chetan", 41)

print(student.name)
print(student.age)
```

Explain:

- `__init__` runs automatically when an object is created
- `name` and `age` are parameters
- `self.name` and `self.age` are attributes belonging to that object

Show:

```python
student = Student("Chetan", 41)
```

Conceptually:

```text
Student(...)
    ↓
__init__(...)
    ↓
self.name = "Chetan"
self.age = 41
```

## Explain `self`

Keep the explanation practical.

When we write:

```python
student = Student("Chetan", 41)
```

Python creates the object and `self` refers to that particular object inside its methods.

So:

```python
self.name = name
```

means:

> Store this student's name inside this particular Student object.

Do not turn `self` into a deep language-internals discussion.

---

# Part D — Add All Student Data

Expand the class:

```python
class Student:
    """Represent a student."""

    def __init__(
        self,
        name,
        age,
        python,
        mathematics,
        communication,
    ):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication
```

Create an object:

```python
student = Student(
    "Chetan",
    41,
    85,
    78,
    90,
)
```

Display the attributes:

```python
print("Name:", student.name)
print("Age:", student.age)
print("Python:", student.python)
print("Mathematics:", student.mathematics)
print("Communication:", student.communication)
```

Ask:

> Where is all the data now?

Answer:

> Inside one `Student` object.

This is the first major improvement over the dictionary approach.

---

# Part E — Add Behavior with Methods

The student object currently stores data.

Ask:

> What about the behavior that belongs to a student?

For example:

```text
Student
├── name
├── age
├── python
├── mathematics
├── communication
└── calculate_percentage()
```

Add:

```python
def calculate_percentage(self):
    total = (
        self.python
        + self.mathematics
        + self.communication
    )

    return total / 3
```

The complete class becomes:

```python
class Student:
    """Represent a student."""

    def __init__(
        self,
        name,
        age,
        python,
        mathematics,
        communication,
    ):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication

    def calculate_percentage(self):
        total = (
            self.python
            + self.mathematics
            + self.communication
        )

        return total / 3
```

Call the method:

```python
student = Student(
    "Chetan",
    41,
    85,
    78,
    90,
)

percentage = student.calculate_percentage()

print("Percentage:", percentage)
```

Explain:

```text
student
  |
  ├── data
  │   ├── name
  │   ├── age
  │   ├── python
  │   ├── mathematics
  │   └── communication
  │
  └── behavior
      └── calculate_percentage()
```

This is the central OOP idea for the workshop:

> **An object combines related data and behavior.**

---

# Part F — Add a `display()` Method

Ask:

> We also need to display a student. Where should that behavior live?

Add:

```python
def display(self):
    print("Name:", self.name)
    print("Age:", self.age)
    print("Python:", self.python)
    print("Mathematics:", self.mathematics)
    print("Communication:", self.communication)
    print("Percentage:", self.calculate_percentage())
```

Now:

```python
student.display()
```

The object is responsible for displaying its own information.

The class now contains:

```text
Student
├── attributes
│   ├── name
│   ├── age
│   ├── python
│   ├── mathematics
│   └── communication
│
└── methods
    ├── calculate_percentage()
    └── display()
```

---

# Part G — Multiple Objects

This is important because it demonstrates why a class is useful.

Create two students:

```python
student1 = Student(
    "Chetan",
    41,
    85,
    78,
    90,
)

student2 = Student(
    "Rahul",
    21,
    72,
    88,
    81,
)
```

Then:

```python
student1.display()

print()

student2.display()
```

Explain:

```text
Student class
      |
      +---- student1
      |
      +---- student2
```

Both objects have the same structure and behavior, but they contain different data.

Ask:

> Did we have to write `calculate_percentage()` twice?

No.

The method is defined once in the class and used by every `Student` object.

This is one of the strongest reasons for using classes.

---

# Part H — Update an Object's Data

Demonstrate that attributes can change:

```python
student1.python = 95
```

Then:

```python
student1.display()
```

The percentage changes automatically because:

```python
calculate_percentage()
```

uses the object's current marks.

Explain:

> The method operates on the data belonging to the particular object that calls it.

---

## Student Exercise

Give students a partially completed class:

```python
class Student:
    """Represent a student."""

    def __init__(
        self,
        name,
        age,
        python,
        mathematics,
        communication,
    ):
        # TODO: Store all student details
        pass

    def calculate_percentage(self):
        """Calculate the student's percentage."""
        # TODO: Calculate and return the percentage
        pass

    def display(self):
        """Display the student's details."""
        # TODO: Display all student details
        pass
```

Ask them to:

1. store the five attributes
2. implement `calculate_percentage()`
3. implement `display()`
4. create one `Student` object
5. call `display()`

Expected solution:

```python
class Student:
    """Represent a student."""

    def __init__(
        self,
        name,
        age,
        python,
        mathematics,
        communication,
    ):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication

    def calculate_percentage(self):
        """Calculate the student's percentage."""
        total = (
            self.python
            + self.mathematics
            + self.communication
        )

        return total / 3

    def display(self):
        """Display the student's details."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Python:", self.python)
        print("Mathematics:", self.mathematics)
        print("Communication:", self.communication)
        print("Percentage:", self.calculate_percentage())


student = Student("Anil", 21, 80, 70, 90)

student.display()
```

Expected output:

```text
Name: Anil
Age: 21
Python: 80
Mathematics: 70
Communication: 90
Percentage: 80.0
```

---

# Part I — Compare Dictionary vs Object

This comparison is useful, but keep it short.

Dictionary approach:

```python
student = {
    "name": "Anil",
    "age": 21,
    "python": 80,
    "mathematics": 70,
    "communication": 90,
}
```

Behavior is outside:

```python
calculate_percentage(student)
display_student(student)
```

Object-oriented approach:

```python
student = Student(
    "Anil",
    21,
    80,
    70,
    90,
)
```

Behavior belongs to the object:

```python
student.calculate_percentage()
student.display()
```

Explain:

```text
Dictionary
    → mainly represents data

Object
    → represents data + related behavior
```

Do not claim that dictionaries are "wrong." Explain that different representations are useful for different purposes.

---

# Part J — Connect OOP to the Application

Now reveal where this is going.

The application will eventually contain:

```text
Student
    ↓
represents one student

StudentManager
    ↓
manages many students

Storage
    ↓
saves and loads students

Main
    ↓
interacts with the user
```

At this stage, only `Student` is introduced.

Ask:

> If `Student` represents one student, who should manage a collection of students?

This creates the need for the next application-design step.

Before introducing `StudentManager`, however, introduce **encapsulation**.

A student currently has attributes that can be changed directly:

```python
student.python = -50
```

Ask:

> Should the application allow any value to be assigned directly?

This creates the problem that encapsulation will address.

---

## Transition to Encapsulation

Show:

```python
student.python = -50

student.display()
```

The program accepts the invalid value.

Ask:

> How can the Student object control how its data is changed?

Introduce the next concept:

> **Encapsulation — keeping data and the operations that control that data together, so that changes can be validated or controlled.**

The progression is now:

```text
Dictionary
    ↓
Class
    ↓
Object
    ↓
Data + behavior
    ↓
Need to control access to data
    ↓
Encapsulation
```

## Instructor Notes

- Keep OOP concrete and application-focused.
- Avoid beginning with definitions of abstraction, polymorphism, interfaces, or design patterns.
- Introduce one idea at a time: class → object → attributes → `__init__` → methods → multiple objects.
- Do not over-explain `self`; students need a practical mental model.
- Use the same Student example throughout the stage.
- Make the difference between class and object explicit several times.
- Emphasize that a method is behavior associated with an object.
- Do not introduce inheritance yet. It comes after encapsulation.
- Avoid private-name conventions such as `__python` at this stage; first establish the basic problem that encapsulation solves.
- The Student class created here should become the actual foundation of the Student Management System later in Day 1.

## Checkpoint

Before moving to Encapsulation, students should be able to answer:

1. What is a class?
2. What is an object?
3. What is an attribute?
4. What is a method?
5. What does `__init__` do?
6. What does `self` refer to?
7. Why can multiple objects be created from one class?
8. Why is `calculate_percentage()` a method rather than a separate function?
9. What is the difference between the Student class and a particular Student object?
10. What problem remains if object attributes can be changed without validation?

## Day 1 Milestone

At the end of this stage, students should have this mental model:

```text
Student class
      |
      +-------------------+
      |                   |
      v                   v
  student1            student2
      |                   |
      +-- data            +-- data
      +-- behavior        +-- behavior
```

The application has now moved from:

```text
functions operating on dictionaries
```

to:

```text
objects containing data and behavior
```

That is the foundation for the remaining OOP and application-design stages.


# Stage 6 — Encapsulation

**Approximate time: 15–20 minutes**

## Objective

Students should understand:

- why object data should sometimes be controlled
- what encapsulation means in practical terms
- how methods can control changes to object data
- why validation can belong inside the class
- how encapsulation protects the object's state
- how this prepares the Student class for a larger application

## Connect from Stage 5

The `Student` class now combines data and behavior:

```python
student = Student(
    "Anil",
    21,
    80,
    70,
    90,
)
```

The object contains:

```text
name
age
python
mathematics
communication
```

and provides:

```text
calculate_percentage()
display()
```

But there is a problem.

Because the attributes are directly accessible, someone can write:

```python
student.python = -50
```

or:

```python
student.python = 150
```

The object accepts both values.

Ask:

> Should every piece of code be allowed to change the student's marks directly?

This creates the need for encapsulation.

## Key message

For this workshop, use a practical definition:

> **Encapsulation means keeping an object's data and the operations that control that data together.**

The important idea is **controlled access**, not simply making variables private.

Show:

```text
Without control

main.py
   ↓
student.python = -50
   ↓
invalid object state
```

versus:

```text
With controlled operation

main.py
   ↓
student.update_python_mark(-50)
   ↓
Student validates the value
   ↓
object remains valid
```

---

## Part A — First Identify the Problem

Start with the existing class.

Demonstrate:

```python
student.python = -50

print(student.python)
```

Output:

```text
-50
```

Ask:

> Who allowed this invalid value?

The answer is:

> The object currently has no control over how its data is changed.

Explain that simply having a class does not automatically provide encapsulation.

---

# Part B — Move the Change Behind a Method

Create a method:

```python
def update_python_mark(self, mark):
    if 0 <= mark <= 100:
        self.python = mark
    else:
        print("Invalid Python mark.")
```

Now use:

```python
student.update_python_mark(95)
```

Then:

```python
student.display()
```

Try an invalid value:

```python
student.update_python_mark(-50)
```

The method rejects it.

Try:

```python
student.update_python_mark(150)
```

Again, the value is rejected.

Explain:

```text
Caller
   ↓
update_python_mark()
   ↓
validation
   ↓
change object state only if valid
```

This is the practical encapsulation pattern students need to understand.

---

## Part C — Explain Why the Method Matters

Compare the two approaches.

Direct modification:

```python
student.python = -50
```

Controlled modification:

```python
student.update_python_mark(-50)
```

The second approach gives the `Student` class responsibility for maintaining its own valid state.

Emphasize:

> **The class knows the rules for its own data.**

This is an important application-design principle that students will use later.

---

## Part D — Apply the Same Idea to Other Marks

If time permits, add:

```python
def update_mathematics_mark(self, mark):
    if 0 <= mark <= 100:
        self.mathematics = mark
    else:
        print("Invalid Mathematics mark.")


def update_communication_mark(self, mark):
    if 0 <= mark <= 100:
        self.communication = mark
    else:
        print("Invalid Communication mark.")
```

Demonstrate:

```python
student.update_mathematics_mark(85)
student.update_communication_mark(92)
```

Then:

```python
student.display()
```

The object now controls how its marks are updated.

Do not spend too much time creating many setter methods. One clear example is enough to establish the concept.

---

# Part E — Connect Encapsulation to Responsibility

Ask:

> Where should the rule "marks must be between 0 and 100" live?

Possible answer:

```text
main.py
```

But explain why that is not ideal.

If multiple parts of the application update marks:

```text
main.py
StudentManager
API integration
future UI
```

each one could implement the validation differently.

Instead:

```text
Student
   ↓
owns student data
   ↓
owns rules for changing that data
```

This gives us a cleaner responsibility boundary.

The concept is:

> **An object should be responsible for maintaining the validity of its own state.**

---

## Student Exercise

Give students the following class:

```python
class Student:
    """Represent a student."""

    def __init__(self, name, python):
        self.name = name
        self.python = python

    def update_python_mark(self, mark):
        # TODO: Allow the update only when mark is between 0 and 100
        pass
```

Ask them to:

1. accept a new mark
2. check whether it is between 0 and 100
3. update the mark if valid
4. display an error message if invalid

Expected solution:

```python
class Student:
    """Represent a student."""

    def __init__(self, name, python):
        self.name = name
        self.python = python

    def update_python_mark(self, mark):
        if 0 <= mark <= 100:
            self.python = mark
        else:
            print("Invalid Python mark.")
```

Test:

```python
student = Student("Anil", 80)

student.update_python_mark(95)
print(student.python)

student.update_python_mark(150)
print(student.python)
```

Expected behavior:

```text
95
Invalid Python mark.
95
```

The second invalid update does not change the existing valid value.

---

# Part F — Clarify What Encapsulation Is Not

This is a useful clarification because students often learn:

> "Encapsulation means making variables private."

Explain that this is an oversimplification.

For this workshop, the important idea is:

```text
Encapsulation
    =
data + controlled operations
```

Python provides conventions and mechanisms for restricting access, but do not turn this session into a detailed discussion of:

```python
_name
__name
@property
getters/setters
```

Those topics are outside the workshop scope.

The students should leave with the application-level understanding:

> Instead of allowing arbitrary code to modify important data, provide operations that control how the data changes.

---

## Part G — Connect Back to Earlier Stages

Make the connection explicit.

### Functions

We learned to isolate reusable logic:

```python
calculate_percentage(...)
```

### Modules

We learned to organize related logic:

```text
student_utils.py
```

### Exceptions

We learned to handle invalid input:

```python
try:
    ...
except ValueError:
    ...
```

### File and JSON

We learned to persist data:

```text
students.json
```

### OOP

We learned to combine data and behavior:

```python
student.calculate_percentage()
```

### Encapsulation

We now control how important object data changes:

```python
student.update_python_mark(95)
```

The concepts are building on one another.

---

## Transition to Inheritance

The `Student` class is now becoming a meaningful model.

Ask:

> Are there other people in our application?

For example:

```text
Student
Teacher
Administrator
```

They may all have common information:

```text
name
age
```

and common behavior:

```text
display()
```

Ask:

> Should we repeat the same code in every class?

This creates the next problem:

```text
Student
    ├── name
    ├── age
    └── display()

Teacher
    ├── name
    ├── age
    └── display()
```

Introduce:

> **Inheritance allows a class to reuse common attributes and behavior from another class.**

This creates the transition:

```text
Encapsulation
    ↓
Related classes
    ↓
Repeated common behavior
    ↓
Inheritance
```

## Instructor Notes

- Keep encapsulation concrete rather than theoretical.
- Use the invalid mark example because students immediately understand why `-50` and `150` are invalid.
- Do not introduce private attributes simply to demonstrate syntax.
- Emphasize that validation is a responsibility of the `Student` object.
- Avoid a long discussion of getters and setters.
- Do not introduce `@property` unless there is extra time and a strong reason.
- Do not introduce custom exceptions.
- Make clear that direct attribute access is being used in the workshop for simplicity; the encapsulation lesson demonstrates controlled updates through methods.
- The goal is to teach the design principle, not every Python mechanism related to encapsulation.

## Checkpoint

Before moving to Inheritance, students should be able to answer:

1. What problem does encapsulation solve?
2. Why is `student.python = -50` a problem?
3. How can a method control changes to an object's data?
4. Why should the `Student` class know the rules for valid marks?
5. What does "controlled access" mean?
6. Is encapsulation simply the same thing as making variables private?
7. How does encapsulation improve the responsibility of the `Student` class?

## Day 1 Milestone

The `Student` class now represents:

```text
Student
├── Data
│   ├── name
│   ├── age
│   ├── python
│   ├── mathematics
│   └── communication
│
└── Behavior
    ├── calculate_percentage()
    ├── display()
    └── update_python_mark()
```

The class now has both **data** and **controlled behavior**.

The next question is how to avoid repeating common code when we introduce other related classes.


# Stage 7 — Inheritance

**Approximate time: 20–25 minutes**

## Objective

Students should understand:

- why inheritance is useful
- what a base class is
- what a derived class is
- how common attributes and behavior can be placed in a parent class
- how `super()` is used
- how a child class can add its own attributes and behavior
- the practical meaning of an **IS-A** relationship
- when inheritance helps and when it should not be forced

## Connect from Stage 6

The `Student` class now contains its own data and behavior.

Ask:

> What other types of people might exist in a student management application?

Possible examples:

```text
Student
Teacher
Administrator
```

Now imagine that both Student and Teacher need:

```text
name
age
display()
```

Without inheritance, we might write:

```python
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
```

Ask:

> Are we repeating code?

Yes.

Ask:

> Can we put the common parts somewhere once and let both classes reuse them?

This creates the need for inheritance.

## Key message

Use the practical definition:

> **Inheritance allows one class to reuse common attributes and behavior from another class.**

Introduce the terminology:

```text
Person
  ↓
Base class / Parent class

Student
  ↓
Derived class / Child class
```

The relationship should be:

> **A Student IS-A Person.**

Similarly:

> **A Teacher IS-A Person.**

This is the simplest test for whether inheritance makes sense.

---

# Part A — Create the Base Class

Start with:

```python
class Person:
    """Represent a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
```

Explain:

```text
Person
├── name
├── age
└── display()
```

The common functionality now lives in one place.

---

# Part B — Create a Child Class

Create:

```python
class Student(Person):
    """Represent a student."""
```

Explain:

```text
Student(Person)
```

means:

> Student inherits from Person.

Add the Student-specific data:

```python
class Student(Person):
    """Represent a student."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
```

Explain the two parts:

```python
super().__init__(name, age)
```

initializes the common Person data.

```python
self.student_id = student_id
```

adds Student-specific data.

The structure is now:

```text
Person
├── name
├── age
└── display()

        ↑ inherits

Student
└── student_id
```

---

# Part C — Use the Inherited Behavior

Create:

```python
student = Student(
    "Chetan",
    41,
    "S001",
)
```

Then:

```python
student.display()
```

Explain:

> We did not define `display()` inside Student, but Student can use it because it inherited the method from Person.

This is the important moment to reinforce:

```text
Student
   ↓
inherits
   ↓
Person.display()
```

---

# Part D — Add Student-Specific Behavior

Add:

```python
def display_student(self):
    self.display()
    print("Student ID:", self.student_id)
```

The complete Student class becomes:

```python
class Student(Person):
    """Represent a student."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        self.display()
        print("Student ID:", self.student_id)
```

Use:

```python
student.display_student()
```

Output:

```text
Name: Chetan
Age: 41
Student ID: S001
```

Explain:

```text
Person
    ↓
common data + behavior

Student
    ↓
reuses common behavior
    +
adds student-specific behavior
```

---

# Part E — Add Another Child Class

Now introduce Teacher:

```python
class Teacher(Person):
    """Represent a teacher."""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display()
        print("Subject:", self.subject)
```

Create:

```python
teacher = Teacher(
    "Anita",
    35,
    "Python",
)
```

Then:

```python
teacher.display_teacher()
```

Output:

```text
Name: Anita
Age: 35
Subject: Python
```

Show the complete relationship:

```text
             Person
            /      \
           /        \
      Student      Teacher
```

Both reuse:

```text
name
age
display()
```

while adding their own information.

---

# Part F — Explain `super()`

Keep this explanation practical.

In:

```python
class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
```

`super()` gives the child class access to the parent implementation.

So:

```python
super().__init__(name, age)
```

means:

> Run the Person initialization logic for this Student object.

Then:

```python
self.student_id = student_id
```

adds the part that belongs specifically to Student.

The same pattern applies to Teacher.

Do not go into Python's method resolution order in this workshop.

---

# Part G — The IS-A Test

This is an important design lesson.

Ask:

> Is a Student a Person?

Yes.

```text
Student IS-A Person
```

Ask:

> Is a Teacher a Person?

Yes.

```text
Teacher IS-A Person
```

Now ask:

> Is a Student a StudentManager?

No.

A StudentManager **manages** students; it is not a student.

This distinction prepares students for the application architecture later.

Explain:

```text
Inheritance
    → IS-A relationship

Composition / ownership
    → HAS-A relationship
```

For example:

```text
StudentManager HAS-A collection of Students
```

This is a very important bridge to the next application-design stage.

---

## Student Exercise

Give students:

```python
class Person:
    """Represent a person."""

    def __init__(self, name, age):
        # TODO: Store name and age
        pass

    def display(self):
        # TODO: Display name and age
        pass


class Student(Person):
    """Represent a student."""

    def __init__(self, name, age, student_id):
        # TODO: Initialize Person
        # TODO: Store student_id
        pass

    def display_student(self):
        # TODO: Display inherited information
        # TODO: Display student ID
        pass
```

Ask students to:

1. complete `Person`
2. initialize the parent using `super()`
3. store `student_id`
4. use the inherited `display()` method
5. create a Student object
6. display it

Expected solution:

```python
class Person:
    """Represent a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    """Represent a student."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        self.display()
        print("Student ID:", self.student_id)


student = Student("Anil", 21, "S001")

student.display_student()
```

Expected output:

```text
Name: Anil
Age: 21
Student ID: S001
```

---

# Part H — Connect Inheritance Back to the Student Application

At this point, make an important distinction.

The workshop's actual Student Management System does **not** need a Person/Student inheritance hierarchy.

Why?

Because the application currently needs one main domain entity:

```text
Student
```

The Person/Student example is being used to teach the inheritance concept.

This prevents students from thinking:

> "Every application must use inheritance."

Instead, explain:

> **Use inheritance when there is a genuine IS-A relationship and meaningful common behavior.**

For the actual application, the more important relationship will be:

```text
StudentManager
      |
      └── students
           ├── Student
           ├── Student
           └── Student
```

That is a **HAS-A** relationship.

This naturally leads to application design.

---

# Part I — Inheritance vs Composition

Keep this short but make the distinction explicit.

### Inheritance

```text
Student IS-A Person
```

The Student class inherits from Person.

### Composition / ownership

```text
StudentManager HAS-A collection of Students
```

The manager contains Student objects.

The upcoming application architecture will use this second relationship heavily.

A useful mental model:

```text
IS-A
  ↓
Inheritance

HAS-A
  ↓
Composition / object ownership
```

Do not introduce advanced composition patterns. The goal is simply to give students the correct mental model before they see `StudentManager`.

---

## Transition to Application Design

Now ask:

> We have learned how to create Student objects. What happens when we need to manage 50 students?

We need something responsible for:

```text
Add student
View students
Find student
Update student
Delete student
```

Ask:

> Should the Student class itself manage all 50 students?

No.

A `Student` should represent **one student**.

We need another responsibility:

```text
Student
    ↓
represents one student

StudentManager
    ↓
manages many students
```

Then we also have:

```text
Storage
    ↓
saves and loads students

Main
    ↓
handles user interaction
```

This creates the final Day 1 concept:

> **Application Design — dividing an application into components with clear responsibilities.**

The progression is now:

```text
OOP
  ↓
Encapsulation
  ↓
Inheritance
  ↓
IS-A vs HAS-A
  ↓
Separate responsibilities
  ↓
Application Design
```

## Instructor Notes

- Use Person → Student/Teacher as a small teaching example, not as the application's main architecture.
- Make `super()` practical and concise.
- Do not introduce multiple inheritance.
- Do not introduce abstract base classes.
- Do not introduce method resolution order.
- Do not force inheritance into the Student Management System.
- Explicitly explain that inheritance is useful only when the relationship and shared behavior make sense.
- Spend time on the **IS-A vs HAS-A** distinction because it directly prepares students for `StudentManager`.
- Keep the application domain simple: `Student` represents one student; `StudentManager` manages many students.
- The actual application will rely more on object composition/ownership than inheritance.

## Checkpoint

Before moving to Application Design, students should be able to answer:

1. What is inheritance?
2. What is a parent/base class?
3. What is a child/derived class?
4. What does `super()` do?
5. What does "Student IS-A Person" mean?
6. Why can Student use `Person.display()`?
7. When does inheritance make sense?
8. Why should we not force inheritance into every application?
9. What is the difference between IS-A and HAS-A?
10. Why is `StudentManager HAS-A collection of Students` rather than an inheritance relationship?

## Day 1 Milestone

Students should now understand:

```text
Class
  ↓
Object
  ↓
Encapsulation
  ↓
Inheritance
```

and, more importantly:

```text
Student
    → one student

StudentManager
    → many students

Storage
    → persistence

Main
    → user interaction
```

The next stage turns these ideas into a real application architecture.


# Stage 8 — Application Design

**Approximate time: 30–35 minutes**

## Objective

Students should understand:

- why a real application needs separation of responsibilities
- how to identify components from the application's requirements
- why one large `main.py` becomes difficult to maintain
- how classes and modules work together
- the difference between an entity, a manager/service, storage, and user interaction
- how the Student Management System can be divided into clear components
- how data flows between the components
- why good application design makes future changes easier

## Connect from Stage 7

Students have now learned:

```text
Functions
Modules
Exceptions
Files
JSON
Classes and Objects
Encapsulation
Inheritance
```

Ask:

> Can we now build the Student Management System in one file?

Technically, yes.

But show the problem.

A single `main.py` could eventually contain:

```text
main.py
├── Student class
├── StudentManager class
├── save_students()
├── load_students()
├── input handling
├── menu
├── validation
├── CRUD operations
└── application loop
```

Ask:

> What happens when this file becomes 500 or 1,000 lines long?

Expected answers:

- difficult to understand
- difficult to test
- difficult to modify
- difficult to find bugs
- different responsibilities become mixed together

Introduce the final Day 1 concept:

> **Application design means dividing a program into components, with each component having a clear responsibility.**

---

# Part A — Start with Requirements

Do not begin by showing the final folder structure.

First ask the students what the application needs to do.

The Student Management System should support:

```text
1. Add Student
2. View Students
3. Find Student
4. Update Student
5. Delete Student
6. Save students
7. Load students
8. Exit
```

Ask:

> Which parts of the program are responsible for these operations?

Let students suggest possibilities.

Then organize the responsibilities.

---

# Part B — Identify the Student Entity

Ask:

> What does one student look like?

We already created:

```python
class Student:
    ...
```

The Student object contains:

```text
name
age
python
mathematics
communication
```

and behavior such as:

```text
calculate_percentage()
display()
update_python_mark()
```

Explain:

> `Student` represents one student. It should not be responsible for managing every student in the application.

This is the first responsibility boundary.

```text
Student
    ↓
Represents one student
```

---

# Part C — Identify the Manager

Now ask:

> If Student represents one student, who manages a collection of students?

Introduce:

```python
class StudentManager:
    """Manage a collection of students."""

    def __init__(self):
        self.students = []
```

Explain:

```text
StudentManager
      |
      └── students
           ├── Student
           ├── Student
           └── Student
```

This is the **HAS-A** relationship from the previous stage:

> `StudentManager HAS-A collection of Students.`

The manager is responsible for collection-level operations:

```text
add_student()
view_students()
find_student()
update_student()
delete_student()
```

It should not be responsible for:

```text
writing JSON files
printing the application menu
making HTTP requests
```

Those are different responsibilities.

---

# Part D — Design the StudentManager

Introduce the manager gradually.

### Add

```python
def add_student(self, student):
    """Add a student to the collection."""
    self.students.append(student)
```

Explain:

> The manager knows how to add a Student to its collection.

### View

```python
def view_students(self):
    """Display all students."""
    if not self.students:
        print("No students found.")
        return

    for student in self.students:
        student.display()
```

Point out the collaboration:

```text
StudentManager
      ↓
iterates over students
      ↓
Student.display()
```

The manager manages the collection; the Student knows how to display itself.

This is an important example of **separation of responsibility**.

---

# Part E — Find

Add:

```python
def find_student(self, name):
    """Find a student by name."""
    for student in self.students:
        if student.name.lower() == name.lower():
            return student

    return None
```

Explain the return values:

```text
Student found
    ↓
return Student object

Student not found
    ↓
return None
```

Ask:

> Why return the Student object instead of printing it inside `find_student()`?

Because the caller may want to do different things with the result:

```text
display it
update it
delete it
```

This is a useful design principle:

> **A function should return information when the caller may need to decide what to do with it.**

---

# Part F — Update

Introduce:

```python
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
```

Explain the collaboration:

```text
StudentManager
      ↓
find Student
      ↓
Student object
      ↓
update its data
```

At this point, remind students about encapsulation.

If the class has controlled update methods, those methods can be used here instead of changing attributes directly.

For the workshop's simple implementation, direct attribute updates may remain in the manager, but point out that the earlier encapsulation lesson shows how those updates could be controlled.

Do not introduce another large refactoring here; the goal is architecture.

---

# Part G — Delete

Add:

```python
def delete_student(self, name):
    """Delete a student by name."""
    student = self.find_student(name)

    if student is None:
        return False

    self.students.remove(student)
    return True
```

Again, the manager is responsible for the collection.

The Student object does not delete itself.

This reinforces:

```text
Student
    → represents one record

StudentManager
    → manages the collection
```

---

# Part H — Identify Storage Responsibility

Now ask:

> Where should `save_students()` and `load_students()` live?

They could be placed in `StudentManager`, but then the manager would have two responsibilities:

```text
1. Manage students
2. Manage files
```

Ask:

> Can we separate persistence from student management?

Introduce:

```text
storage.py
```

with:

```python
save_students()
load_students()
```

Explain:

> `storage.py` is responsible for persistence, not business operations.

The conceptual structure becomes:

```text
Student
    ↓
one student

StudentManager
    ↓
collection + CRUD

Storage
    ↓
JSON persistence

Main
    ↓
user interaction
```

---

# Part I — Identify the Main Program

Now ask:

> Who should interact with the user?

Introduce:

```text
main.py
```

Its responsibility is:

```text
display menu
    ↓
read choice
    ↓
call the appropriate component
    ↓
display result
```

It should not contain the implementation of every operation.

For example:

```python
manager.add_student(student)
```

rather than implementing the list manipulation directly inside `main.py`.

This is a major design improvement.

---

# Part J — Draw the Architecture

Now show the complete architecture.

```text
                    main.py
                       |
          +------------+------------+
          |            |            |
          v            v            v
      Student     StudentManager  Storage
          |            |            |
          |            |            |
          |            v            v
          |         Students     students.json
          |
          v
     Student data
     + behavior
```

Then simplify it for students:

```text
             main.py
                |
       -------------------
       |        |        |
       v        v        v
    Student  Manager  Storage
                 |
                 v
             Students
                 |
                 v
            students.json
```

Explain the direction:

```text
main.py
   ↓
uses components

StudentManager
   ↓
manages Student objects

Storage
   ↓
persists data

Student
   ↓
represents one student
```

This is the application architecture they will implement.

---

# Part K — Map Components to Files

Now reveal the actual project structure.

For the instructor implementation:

```text
application/
├── main.py
├── student.py
├── student_manager.py
└── storage.py
```

Explain:

```text
student.py
    → Student class

student_manager.py
    → StudentManager class

storage.py
    → save/load functions

main.py
    → application flow and user interaction
```

This is where the earlier **Modules** lesson becomes concrete.

Students should now see that the module concept was not taught in isolation.

---

# Part L — Show the Imports

`main.py` will use:

```python
from student import Student
from student_manager import StudentManager
from storage import load_students, save_students
```

Explain:

```text
main.py
   |
   +── imports Student
   +── imports StudentManager
   └── imports storage functions
```

The application is now assembled from smaller components.

---

# Part M — Persistence Flow

Show what happens when the application starts:

```text
Start application
      ↓
load_students()
      ↓
students.json
      ↓
Student objects
      ↓
StudentManager
```

Then when a student is added:

```text
User
 ↓
main.py
 ↓
Student
 ↓
StudentManager
 ↓
save_students()
 ↓
students.json
```

This connects the OOP and JSON concepts from earlier stages.

---

# Part N — CRUD

Now introduce the term **CRUD**.

```text
C → Create
R → Read
U → Update
D → Delete
```

Map it to the application:

| CRUD | Application operation |
|---|---|
| Create | Add Student |
| Read | View / Find Student |
| Update | Update Student |
| Delete | Delete Student |

Explain:

> CRUD is a common pattern in applications that manage records.

The Student Management System is therefore no longer just a collection of Python examples. It is a small CRUD application.

---

# Part O — Build the Application Incrementally

Do not present the entire final application immediately.

Build it in this order:

### Step 1 — Student

Create:

```text
student.py
```

Implement:

```text
Student
calculate_percentage()
display()
```

### Step 2 — StudentManager

Create:

```text
student_manager.py
```

Implement:

```text
add_student()
view_students()
find_student()
update_student()
delete_student()
```

### Step 3 — Storage

Create:

```text
storage.py
```

Implement:

```text
save_students()
load_students()
```

### Step 4 — Main

Create:

```text
main.py
```

Connect the components.

### Step 5 — Test the application

Run:

```text
Add
View
Find
Update
Delete
Exit
```

Then restart the application and confirm persistence.

This gives students a clear implementation sequence.

---

# Part P — Student Exercise

For the application-design exercise, do not ask students to write the entire application from scratch.

Give them a component map:

```text
student.py
student_manager.py
storage.py
main.py
```

Ask them to match each responsibility:

```text
Represent one student
Manage student collection
Save/load JSON
Handle menu and user interaction
```

Expected mapping:

```text
student.py
    → Represent one student

student_manager.py
    → Manage student collection

storage.py
    → Save/load JSON

main.py
    → Menu and user interaction
```

Then ask:

> Which component should be responsible for adding a student?

Answer:

```text
StudentManager
```

> Which component should save the data?

Answer:

```text
Storage
```

> Which component should display the menu?

Answer:

```text
Main
```

> Which component represents one student?

Answer:

```text
Student
```

This exercise checks whether students understand the architecture before they start coding.

---

# Part Q — Instructor Live Build

This is the point where the instructor should begin assembling the actual application.

Use the previously developed files as the reference implementation:

```text
student.py
student_manager.py
storage.py
main.py
```

Do not type every line silently.

Instead, narrate the responsibility as each component is introduced:

```text
"I need something to represent one student."
        ↓
Student

"I need something to manage many students."
        ↓
StudentManager

"I need something to persist the collection."
        ↓
Storage

"I need something to interact with the user."
        ↓
Main
```

This keeps the architecture understandable rather than making the class/module structure feel arbitrary.

---

# Part R — Final Application Flow

Once the components are connected, show the complete flow.

### Application startup

```text
main.py
   ↓
load_students()
   ↓
storage.py
   ↓
students.json
   ↓
Student objects
   ↓
StudentManager
```

### Add Student

```text
User
 ↓
main.py
 ↓
create Student
 ↓
StudentManager.add_student()
 ↓
Storage.save_students()
 ↓
students.json
```

### Find Student

```text
User
 ↓
main.py
 ↓
StudentManager.find_student()
 ↓
Student object
 ↓
Student.display()
```

### Update Student

```text
User
 ↓
main.py
 ↓
StudentManager.update_student()
 ↓
Storage.save_students()
```

### Delete Student

```text
User
 ↓
main.py
 ↓
StudentManager.delete_student()
 ↓
Storage.save_students()
```

This is the complete Day 1 application architecture.

---

# Part S — Final Demonstration

Run the application and demonstrate the complete CRUD flow.

Use a small number of students so the demonstration stays focused.

Recommended sequence:

```text
1. Add Student
2. Add another Student
3. View Students
4. Find Student
5. Update Student
6. View Students again
7. Delete Student
8. View Students again
9. Exit
10. Restart application
11. View Students
```

The restart is important.

It demonstrates:

```text
Application
    ↓
Storage
    ↓
Persistence
```

Students should see that the data survives after the Python process ends.

---

# Stage 8 Teaching Message

The main lesson of this stage is not the number of files.

It is:

> **Each component should have a clear responsibility.**

A useful summary:

```text
Student
    → What is one student?

StudentManager
    → How do we manage many students?

Storage
    → How do we persist them?

Main
    → How does the user interact with the application?
```

This is the foundation of maintainable application design.

---

## Transition to the Final Day 1 Application

At this point, students have all the concepts required to understand the application:

```text
Functions
    ↓
Modules
    ↓
Exceptions
    ↓
File handling
    ↓
JSON
    ↓
Classes and Objects
    ↓
Encapsulation
    ↓
Inheritance
    ↓
Application Design
    ↓
Student Management System
```

The application is now the place where all the concepts meet.

The next step is not a new Python concept.

It is **building and running the application**.

---

## Instructor Notes

- Do not introduce architecture before students understand the underlying concepts.
- This stage should feel like the answer to the question: "How do all these concepts fit together?"
- Start from requirements, not from a folder tree.
- Identify responsibilities before showing files.
- Explicitly connect modules to the earlier Modules lesson.
- Explicitly connect persistence to File/JSON handling.
- Explicitly connect `Student` to Classes and Objects.
- Explicitly connect `StudentManager` to the IS-A/HAS-A discussion.
- Keep `main.py` focused on orchestration and user interaction.
- Do not introduce MVC, dependency injection, repositories, service layers, or enterprise architecture patterns.
- Do not introduce `src` layouts or packaging configuration during this workshop.
- The goal is a simple, understandable architecture that students can implement themselves.
- Use the architecture diagram repeatedly while coding so students understand why each file exists.

## Checkpoint

Before moving into the final application build, students should be able to answer:

1. Why should we avoid putting the whole application in one file?
2. What is the responsibility of `Student`?
3. What is the responsibility of `StudentManager`?
4. What is the responsibility of `storage.py`?
5. What is the responsibility of `main.py`?
6. What is the relationship between StudentManager and Student?
7. What does CRUD mean?
8. Where should saving/loading JSON happen?
9. Why should `find_student()` return a Student object?
10. How does data move from the user to the JSON file?

## Day 1 Milestone

Students should now have the complete mental model:

```text
                    Student Management System
                              |
        +---------------------+---------------------+
        |                     |                     |
        v                     v                     v
     Student            StudentManager           Storage
        |                     |                     |
        |                     |                     |
   one student          many students         JSON file
        |                     |
        +----------+----------+
                   |
                   v
                main.py
                   |
                   v
                 User
```

The architecture is intentionally simple:

> **One responsibility per component, with components collaborating through clear interfaces.**

At the end of Day 1, students should understand not only how to write the code, but **why the code is divided this way**.
