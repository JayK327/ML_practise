import multiprocessing
import time

def square_number():
    for i in range(1,6):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_number():
    for i in range(1,6):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__=="__main__":
    #create 2 processes
    p1=multiprocessing.Process(target=square_number)
    p2=multiprocessing.Process(target=cube_number)
    start_time=time.time()  

    #Start the process  
    p1.start()
    p2.start()
    #Wait for both processes to complete
    p1.join()
    p2.join()
    finished_time=time.time()-start_time
    print(f"Time taken with multiprocessing: {finished_time} seconds")
