class Employee:
   def __init__(self, name, salary):
       self.name = name
       self.__salary = salary  # Private attribute

   def display_salary(self):
        print(f"Salary: {self.__salary}")
        
        
employee = Employee("Yash", 50000)

employee.display_salary()