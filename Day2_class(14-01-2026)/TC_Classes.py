class Student:
    name = "Ravi"
    age = 25

s1 = Student()

print(s1.name)
print(s1.age)

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
e1 = Employee("Ravi",25)
e1.display()

print(e1.name)