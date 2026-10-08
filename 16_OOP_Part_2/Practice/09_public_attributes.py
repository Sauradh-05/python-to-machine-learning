class Student:
    def __init__(self, name):
        self.name = name


student = Student("Yash")

print(student.name)

student.name = "Pratik"

print(student.name)