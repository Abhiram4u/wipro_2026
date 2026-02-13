import math
import time
import multiprocessing


numbers = [50000, 60000, 55000, 45000, 70000]



# factorial digit calculation

def factorial_digits(n):
    digits = math.floor(math.lgamma(n + 1) / math.log(10)) + 1
    return (n, digits)



# Main Program
# -----------------------------------
if __name__ == "__main__":


    # Sequential Computation
    print("\n--- Sequential Factorial Computation Started ---")

    start_time = time.time()

    sequential_results = []
    for num in numbers:
        sequential_results.append(factorial_digits(num))

    sequential_time = time.time() - start_time

    print("\nSequential Results:")
    for n, digits in sequential_results:
        print(f"Factorial of {n} has {digits} digits")

    print(f"\nSequential Time Taken: {sequential_time:.4f} seconds")



    # Multiprocessing Computation
    print("\n--- Multiprocessing Factorial Computation Started ---")

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        parallel_results = pool.map(factorial_digits, numbers)

    multiprocessing_time = time.time() - start_time

    print("\nMultiprocessing Results:")
    for n, digits in parallel_results:
        print(f"Factorial of {n} has {digits} digits")

    print(f"\nMultiprocessing Time Taken: {multiprocessing_time:.4f} seconds")


    
    # Final Comparison

    print("\n--- Time Comparison ---")
    print(f"Sequential Time      : {sequential_time:.4f} seconds")
    print(f"Multiprocessing Time : {multiprocessing_time:.4f} seconds")
