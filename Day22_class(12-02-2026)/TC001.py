import mysql.connector

host = "localhost"
user = "root"
password = "0609"

database = "wipro2026"

conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

cursor = conn.cursor()
print("connected to the database successflly")

cursor.execute("select * from employee")
result = cursor.fetchall()

for row in result:
    print(row)