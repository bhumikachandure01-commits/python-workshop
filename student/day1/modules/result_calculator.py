# TODO
def calculate_percentage(marks_python,marks_math,marks_comm):
        total= (marks_comm+marks_math+marks_python)
        percentage = (total/300)*100
        return percentage
      

def calculate_grade(percentage):
    grade=none
    if percentage>=80:
        grade="A"
    if percentage>=60:
        grade="B"
    if percentage>=40:
        grade="c"
    else:
        grade="d"
    return grade    
