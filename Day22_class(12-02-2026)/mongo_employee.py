from pymongo import MongoClient

# ---------------------------------------
# 1. Connect to Local MongoDB
# ---------------------------------------

client = MongoClient("mongodb://localhost:27017/")

db = client["company_db"]
employees = db["employees"]

print("Connected to MongoDB successfully!")


#2---
print("\n--- Inserting New Employee ---")

new_employee = {
    "name": "Rahul",
    "department": "IT",
    "salary": 70000
}

employees.insert_one(new_employee)

print("Employee Inserted Successfully!")

print("\nAll Employees:")

for emp in employees.find():
    print(emp)


#3-----
print("\n--- Employees in IT Department ---")

for emp in employees.find({"department": "IT"}):
    print(emp)

#4-------
print("\n--- Updating Salary ---")

employees.update_one(
    {"name": "Rahul"},
    {"$set": {"salary": 85000}}
)

print("Salary Updated Successfully!")

print("\n Employees After Update:")

for emp in employees.find():
    print(emp)
