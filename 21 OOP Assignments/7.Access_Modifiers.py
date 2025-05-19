class Employee:

    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

x = Employee("Ali", 100000, '12345678')
print(x.name) #No errors were found can easily access public variable outside the class
print(x._salary)  #No errors were found can easily access protected variable outside the class
print(x.__ssn)  #Error orcured cannot access private variable outside the class
print(x._Employee__ssn) # We can access private variable using this method