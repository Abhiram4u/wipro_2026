import mysql.connector

# Database Connection

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0609",
    database="company_db"
)

cursor = connection.cursor()

print("Connected to MySQL Database Successfully!")
# -------------------------------
# Function to Display Table Rows
# -------------------------------
def show_employees():
    print("\nCurrent Employees Table:")
    cursor.execute("SELECT * FROM employes")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

# ---------------------------
# 1
print("\n--- Employees with Salary > 50000 ---")

query = "SELECT * FROM employes WHERE salary > 50000"
cursor.execute(query)

result = cursor.fetchall()

for row in result:
    print(row)

# # 2
print("\n--- Inserting New Employee ---")

insert_query = """
INSERT INTO employes (name, department, salary)
VALUES (%s, %s, %s)
"""

new_employee = ("Rahul", "IT", 72000)

cursor.execute(insert_query, new_employee)
connection.commit()
# show full table
show_employees()

# -----------------------
# 3
print("\n--- Updating Employee Salary by 10% ---")

employee_id = 5

update_query = """
UPDATE employes
SET salary = salary * 1.10
WHERE id = %s
"""

cursor.execute(update_query, (employee_id,))
connection.commit()

print(f"Salary updated successfully for employee ID {employee_id}")

show_employees()