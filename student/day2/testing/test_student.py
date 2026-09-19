import unittest

from student.day2.application.student import Student


class TestStudent(unittest.TestCase):
    """Test the Student class."""

    def test_calculate_percentage(self):
        student = Student("Anil", 21, 80, 70, 90)

        percentage = student.calculate_percentage()

        self.assertEqual(percentage, 80)


if __name__ == "__main__":
    unittest.main()
