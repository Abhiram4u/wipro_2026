# Topic: Iterators & Generators
#
# 1. Create a custom  iterator class that iterates over numbers from 1 to N

class Number_Iterator:
    def __init__(self,n):
        self.n = n
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

itr = Number_Iterator(7)
for i in itr:
    print(i)


# 2. Create a generator function that yields the first N Fibonacci numbers
def fib(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a, b = b, a+b
for num in fib(5):
    print(num)

# 3. Demonstrate the difference between using the iterator and generator by printing values using a for loop
print("Iterator Ourput:")
itr = Number_Iterator(7)
for num in itr:
    print(num)

print("\nGenerator Ourput:")
for i in fib(5):
    print(i)
