class Parent:
    def parent(self):
        print("Parent class")
class Child1(Parent):
    def c1(self):
        print("child 1")
class Child2(Parent):
    def c2(self):
        print("child 2")

c1 = Child1()
c1.c1()

c2 = Child2()
c2.c2()