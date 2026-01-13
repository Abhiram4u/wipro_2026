# Topic: range, enumerate, iter, map, filter, reduce, lambda
# Write a Python program that:

# 1. Uses range() to generate numbers from 1 to 20
numbers = range(1,21)

# 2. Uses filter() with a lambda to select only even numbers
even_numbers = list(filter(lambda x: x%2==0,numbers))
print(even_numbers)

# 3. Uses map() with a lambda to square the filtered numbers
square_even_numbers = list(map(lambda x:x**2,even_numbers))
print(square_even_numbers)

# 4. Uses reduce() to calculate the sum of squared even numbers
from functools import reduce
sum_of_squares = reduce(lambda x,y:x+y,square_even_numbers)
print(sum_of_squares)

# 5. Uses enumerate() to print the index and value of the final result list
print(square_even_numbers)
for index,value in enumerate(square_even_numbers):
    print(index,value)