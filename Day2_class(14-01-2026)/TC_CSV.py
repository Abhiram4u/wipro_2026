import csv

with open("student.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name","id","age"])
    writer.writerow(["abhi","101","22"])
    writer.writerow(["john","102","21"])
    writer.writerow(["jane","103","20"])