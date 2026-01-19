from models.student import Student
from models.faculty import Faculty
from models.course import Course
from utils.file_manager import save_students_json, generate_csv_report

students = []
faculty_list = []
courses = []

def student_generator():
    print("Student Record Generator")
    print("Fetching Student Records...")
    print("--------------------------------")
    for s in students:
        yield f"{s.pid} - {s.name}"

while True:
    print("""
1 → Add Student
2 → Add Faculty
3 → Add Course
4 → Enroll Student to Course
5 → Calculate Student Performance
6 → Compare Two Students
7 → Generate Reports
8 → Exit
""")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            sid = input("Student ID: ")
            if any(s.pid == sid for s in students):
                raise Exception("Student ID already exists")

            name = input("Student Name: ")
            dept = input("Department: ")
            sem = int(input("Semester: "))
            marks = list(map(int, input("Enter 5 marks: ").split()))

            student = Student(sid, name, dept, sem, marks)
            students.append(student)

            print("Student Created Successfully")
            print("--------------------------------")
            print(f"ID        : {sid}")
            print(f"Name      : {name}")
            print(f"Department: {dept}")
            print(f"Semester  : {sem}")

        elif choice == "2":
            fid = input("Faculty ID: ")
            name = input("Faculty Name: ")
            dept = input("Department: ")
            salary = int(input("Monthly Salary: "))

            faculty = Faculty(fid, name, dept, salary)
            faculty_list.append(faculty)

            print("Faculty Created Successfully")
            print("--------------------------------")
            print(f"ID        : {fid}")
            print(f"Name      : {name}")
            print(f"Department: {dept}")

        elif choice == "3":
            code = input("Course Code: ")
            cname = input("Course Name: ")
            credits = int(input("Credits: "))
            faculty = faculty_list[0]

            course = Course(code, cname, credits, faculty)
            courses.append(course)

            print("Course Added Successfully")
            print("--------------------------------")
            print(f"Course Code : {code}")
            print(f"Course Name : {cname}")
            print(f"Credits     : {credits}")
            print(f"Faculty     : {faculty.name}")

        elif choice == "4":
            students[0].enroll_course(courses[0])

            print("Enrollment Successful")
            print("--------------------------------")
            print(f"Student Name : {students[0].name}")
            print(f"Course       : {courses[0].name}")


        elif choice == "5":

            key = input("Enter Student ID or Name: ").strip().lower()

            found = False

            for s in students:

                if s.pid.lower() == key or s.name.lower() == key:
                    avg, grade = s.calculate_performance()

                    print("Student Performance Report")

                    print("--------------------------------")

                    print(f"Student Name : {s.name}")

                    print(f"Marks        : {s.marks}")

                    print(f"Average      : {avg}")

                    print(f"Grade        : {grade}")

                    found = True

                    break

            if not found:
                print("Error: Student not found")


        elif choice == "6":
            print("Comparing Students Performance")
            print("--------------------------------")
            print(f"{students[0].name} > {students[1].name} : {students[0] > students[1]}")

        elif choice == "7":
            for rec in student_generator():
                print(rec)
            generate_csv_report(students)
            save_students_json(students)

        elif choice == "8":
            print("Thank you for using Smart University Management System")
            break

    except Exception as e:
        print("Error:", e)
