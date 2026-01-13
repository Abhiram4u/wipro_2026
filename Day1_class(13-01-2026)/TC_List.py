numbers = [10,20,30,40]
names = ["abhi","saritha","arjun","varun"]

mixed = [1,"python",2.5,True]

numbers[1] = 100
print(numbers)
print(names)
print(mixed)

for i in numbers:
    print(i)

if 10 in numbers:
    print("Found 10")
else:
    print("no")

matrix = [[1,2,3],[4,5,6]]
print(matrix[1][2])

names.reverse()
print(names)
names.append("karan")
print(names)

names.extend(["sharan","charan"])
print(names)

names.remove("karan")
print(names)

names.insert(3,'karna')
print(names)

