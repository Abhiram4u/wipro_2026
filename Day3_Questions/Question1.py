import time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@execution_time
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
print(factorial(10))
