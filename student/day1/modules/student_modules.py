from result_calculator import calculate_percentage
# Day 1 - Python Fundamentals

student_name = input("Enter student name:")
marks_python = float(input("Enter marks for Python:"))
marks_math = float(input("Enter marks for Mathematics:"))
marks_comm = float(input("Enter marks for Communication:"))
def input_student():
    student_name=input("enter student name:")
    marks_python=float(input("enter marks of python"))
    marks_math=float(input("enter maks of math")) 
    marks_comm=float(input("marks of communication"))
    dict_student_info ={
        "name":student_name,
        "python_marks":marks_python,
        "math_marks":marks_math,
        "comm_marks":marks_comm,
    }
    #return student_name,marks_python,marks_math,marks_comm return dict_student_info
    return dict_student_info

#TODO:
#Create a function to calculate the percentage
#TODO


percentage = 0
if __name__=="__main__":
        print("\n-- Result--")
        student_info = input_student()
        #name,python_m,math_m,comm_m =input_student()
        print(student_info)
        print("student:", student_info["name"])
        print("percentage", calculate_percentage(                                  
        student_info["python_marks"],
        student_info["math_marks"],
        student_info["comm_marks"])
        )

