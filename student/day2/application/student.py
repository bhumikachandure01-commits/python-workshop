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
        total = self.python + self.mathematics + self.communication

        return total / 3
    
    def grade(self):
        self.calculate_percentage()
        if percentage>=80:
            grade="A"
        if percentage>=60:
            grade="B"
        if percentage>=40:
            grade="c"
        else:
            grade="d"
            return grade    

    def display(self):
        """Display the student's details."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Python:", self.python)
        print("Mathematics:", self.mathematics)
        print("Communication:", self.communication)
        print("Percentage:", self.calculate_percentage())
        print("grade",self(grade))

if __name__ == "__main__":
    Student__obj1 = Student("bhumika",20,30,40,50)
    Student__obj2 = Student("bhuvan",18,30,40,50)
    Student__obj3 = Student("deeksha",19,20,40,50)
    Student__obj4 = Student("vismaya",19,30,40,50)
    Student__obj5 = Student("ATHARV",19,40,50,60)
    Student__obj1.display()
    Student__obj2.display()
    Student__obj3.display()
    Student__obj4.display()
    Student__obj5.display()

