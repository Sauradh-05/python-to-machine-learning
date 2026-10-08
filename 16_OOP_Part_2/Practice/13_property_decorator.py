class Student:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks.")


student = Student(80)

print("Marks:", student.marks)

student.marks = 95

print("Updated Marks:", student.marks)