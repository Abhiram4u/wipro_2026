class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    def display_details(self):
        print("Name:",self.name)
        print("Roll no:",self.roll_no)

s1 = Student("abhi",1)
s2 = Student("arun",2)
s1.display_details()
s2.display_details()



