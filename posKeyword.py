# * is used before argument to pass unknown no. of arguments
# ** is used to recieve dictionary in function

import sys 
def student_info(*args , **kwargs):
    print(args)
    print(kwargs)

name = "Ajay"
course = "ECE"
marks = {
    "Maths": 90,
    "English" : 87,
    "Physics" : 91
}

marks2 = {
    "Biology" : 72,
    "Chemistry" : 78
}

student_info(name,course,**marks2,**marks)

print(sys.path)