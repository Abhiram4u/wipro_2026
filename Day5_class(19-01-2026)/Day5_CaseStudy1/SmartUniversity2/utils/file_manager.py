import json
import csv
import os

DATA_PATH = "data"

def save_students_json(students):
    data = []
    for s in students:
        avg, grade = s.calculate_performance()
        data.append({
            "id": s.pid,
            "name": s.name,
            "department": s.department,
            "average": avg,
            "grade": grade
        })

    with open(f"{DATA_PATH}/students.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Student data successfully saved to students.json")


def generate_csv_report(students):
    with open(f"{DATA_PATH}/students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students:
            avg, grade = s.calculate_performance()
            writer.writerow([s.pid, s.name, s.department, avg, grade])

    print("CSV Report generated successfully")
