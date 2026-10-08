class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")


student = Student("Sauradh")

student.display_name()
student.study()