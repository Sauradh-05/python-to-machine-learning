class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

employee1 = Employee("Yash", 1007, 85000)
employee1.display()
