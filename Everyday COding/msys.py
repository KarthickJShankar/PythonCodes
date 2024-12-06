# import time
# def decorator(func):
#     def wrapper(a):
#         current_time = time.time()
#         print(current_time)
#         time_difference = current_time-(30*12*60*60)
#         print(time.ctime(time_difference))
#         val = func(a)
#         return val*val
#     return wrapper
# @decorator
# def calculate(a):
#     return 2*a
#
# print(calculate(3))
#
# def is_palindrom(num):
#     original = num
#     reversed_num = 0
#     while num>0:
#         last_digit = num%10
#         reversed_num = reversed_num*10+last_digit
#         num = num//10
#     return original==reversed_num
#
# print(is_palindrom(111))
#
#
# def solution(arr):
#     for n in arr:
#         yield(n)
# g = solution([1,2,3,4,5])
# print(g)
# for n in g:
#     print(n,end =' ')

# class ContextManagement():
#     def __init__(self,file_mode,file_name):
#         self.file_mode = file_mode
#         self.file_Name = file_name
#         self.file = None
#     def __enter__(self):
#         self.file = open(self.file_Name,self.file_mode)
#         return self.file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
#
# with ContextManagement("w","test.txt") as file:
#     file.write("test")


# from multiprocessing import Process
#
# import time
#
# def calculate(a):
#     time.sleep(2)
#     print(a)
# processes = []
# for i in range(10):
#     process = Process(target=calculate,args=(i,))
#     processes.append(process)
#     process.start()
# for process in processes:
#     process.join()

# from threading import Thread
# def calculate(a):
#     time.sleep(2)
#     print(a)
# for i in range(10):
# threads = Thread(target=calculate,args=(i,))
# threads.start()
# for threads in threadses:
#     threads.join()

from multiprocessing import Process
import time

# Function that simulates a task by sleeping for 2 seconds and then prints the value of a
def calculate(a):
    time.sleep(2)
    print(a)

processes = []  # List to hold all processes

# Loop to create and start 10 processes
for i in range(10):
    process = Process(target=calculate, args=(i,))  # Create a new process that will run `calculate(i)`
    processes.append(process)  # Add the process to the list
    process.start()  # Start the process

# Wait for all processes to complete before exiting the main program
for process in processes:
    process.join()  # Ensure the main program waits for all processes to finish

# import time
# time_difference = time.time()-(10*12*60*60)
# print(time_difference)
# print(time.ctime(time_difference))