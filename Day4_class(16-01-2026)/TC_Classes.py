class Student:
    name = "abhi"
    def display(self):
        print("this is student class")

s1 = Student()
s1.display()
print(s1.name)
print(Student.name)

class calculater:
    def add(self,a,b):
        print("sum: ",a+b)
c = calculater()
c.add(20,10)