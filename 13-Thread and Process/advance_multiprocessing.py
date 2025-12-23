# With thread pool executor
from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"squared_number :{number}"

numbers=[1,2,3,4,5]

if __name__=="__main__":
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=5) as executor:
        results=executor.map(square_number,numbers)
    end_time = time.time()

    for result in results:
        print(result)

    # total_time = end_time - start_time
    # print(f"Time taken with ThreadPoolExecutor: {total_time:.2f} seconds")

    print(f"Time_taken :{end_time-start_time}")