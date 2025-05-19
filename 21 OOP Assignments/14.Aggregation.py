class Department:
    def __init__(self, employee):
        self.employee = employee

class Employee:
    def __init__(self, name):
        self.name = name

x = Employee("Ali")
y = Department(x)
print(y.employee.name)
        