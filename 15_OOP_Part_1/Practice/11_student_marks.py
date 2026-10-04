class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
    
    def display_result(self):
        print(f"Student: {self.name}")
        print(f"Average Marks: {self.calculate_average():.2f}")
        
student1 = Student("Pratik", [85, 90, 78, 92, 88])
student1.display_result()