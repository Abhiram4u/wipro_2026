from models.person import Person
from utils.descriptors import MarksDescriptor
from utils.decorators import log_execution

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def marks_generator(self):
        for m in self.marks:
            yield m

    @log_execution
    def calculate_performance(self):
        total = sum(self.marks_generator())
        avg = round(total / len(self.marks), 1)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def get_details(self):
        print("Student Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department}")

    def __gt__(self, other):
        return self.calculate_performance()[0] > other.calculate_performance()[0]
