#Multiprocessing for CPU bound tasks
#Factorial calculation : Using multi-processing to calculate factorial of large numbers concurrently to speed up computation.
#Multiprocessing can help to distribute the computation across multiple CPU cores,thereby reducing overall time taken to compute factorials.

import multiprocessing
import time
import math
import sys

sys.set_int_max_str_digits(1000000)  # Increase the limit for large factorial calculations

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is: {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,7000,8000,9000]
    start_time=time.time()
    with multiprocessing.Pool(processes=5) as pool:
        results=pool.map(compute_factorial,numbers)
    end_time=time.time()
    print(f"Time taken with multiprocessing: {end_time-start_time} seconds")
    


# def compute_factorial(number):
#     print(f"Computing factorial of {number}")
#     result = math.factorial(number)
#     print(f"Factorial of {number} is of length: {result.bit_length()} bits")
#     return result

# if __name__ == "__main__":
#     numbers = [5000, 6000, 7000, 8000, 9000]
    
#     start_time = time.time()
    
#     # Use a for loop to compute the factorials sequentially
#     results = []
#     for number in numbers:
#         result = compute_factorial(number)
#         results.append(result)
    
#     end_time = time.time()
#     print(f"Time taken with for loop: {end_time - start_time} seconds")