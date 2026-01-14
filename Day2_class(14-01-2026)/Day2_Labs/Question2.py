# Create a class Employee with attributes:
#     name
#     salary
#
#     Implement a descriptor that:
# 1. Ensures salary is always a positive number
# 2. Raises a ValueError if a negative salary is assigned
# 3. Demonstrates the descriptor by creating multiple Employee objects



class PositiveSalary:
    def __init__(self):
        self._salary = {}
    def __get__(self, instance, owner):
        return self._salary.get(instance,0)
    def __set__(self, instance, value):
        if value<=0:
            raise ValueError('Salary cannot be negative')
        self._salary[instance] = value


class Employee:
    salary = PositiveSalary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("abhi", 100000)
emp2 = Employee("ram", 200000)

print(emp1.name,emp1.salary)
print(emp2.name,emp2.salary)

