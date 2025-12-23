# With thread pool executor
from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    print(f"Number :{number}")

numbers=[1,2,3,4,5,6,7,8,9,0]

start_time = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers,numbers)
end_time = time.time()

for result in results:
    pass

# total_time = end_time - start_time
# print(f"Time taken with ThreadPoolExecutor: {total_time:.2f} seconds")

print(f"Time_taken :{end_time-start_time}")