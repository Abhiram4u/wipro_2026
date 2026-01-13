# Question – List, Dictionary & Set Comprehensions
# Topic: Comprehensions in Python
# Given a list:

data = [1, 2, 3, 4, 5, 6, 2, 4]

# Write a program to:
# 1. Create a list comprehension to store squares of all numbers
squares = [x**2 for x in data]
print(squares)

# 2. Create a set comprehension to store only unique even numbers
unique_even = {x for x in data if x%2==0}
print(unique_even)

# 3. Create a dictionary comprehension where the key is the number and the value is its cube
cube_dict = {x: x**3 for x in data}
print(cube_dict)