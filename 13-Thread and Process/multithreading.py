import threading
import time

def print_number():
    for i in range(1,6):
        time.sleep(1)
        print(f"Number: {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(1)
        print(f"Letter: {letter}")

#create 2 thread
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)


start_time=time.time()
#Start the thread
t1.start()
t2.start()
#Wait for both threads to complete
t1.join()
t2.join()
finished_time=time.time()-start_time
print(f"Time taken without threading: {finished_time} seconds")