students = {
    "name":"abhi",
    "age":22,
    "course":"python"
}

print(students)
print(students["name"])
print(students["age"])
print(students.get("age"))

students["marks"] = 88
students["age"] = 25
print(students)

students.pop("age")
print(students)
students.popitem()
print(students)

print(students.keys())
print(students.values())

for key in students:
    print(key,students[key])
if "name" in students:
    print("found")

employees = {
    101:{"name":"abhi","salary":25000},
    102:{"name":"arun","salary":22000},
    103:{"name":"varun","salary":20000}
}

print(employees[101])
print(employees[102])
print(employees[103])

print(employees[101]["name"])

print(employees[102]["salary"])