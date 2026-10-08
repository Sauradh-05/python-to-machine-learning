class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def work(self):
        print(f"{self.name} is working.")


class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code.")


class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing interfaces.")


developer = Developer("Yash", 60000)
designer = Designer("Suyash", 55000)

employees = [developer, designer]

for employee in employees:
    employee.work()
    print("Salary:", employee.get_salary())