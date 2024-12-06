from threading import Thread
import time
def calculate(a):
    time.sleep(5)
    print(f"Inside Calculate Function {a}")
threads = []
for i in range(10):
    thread = Thread(target=calculate,args=(i,))
    threads.append(thread)
    thread.start()

for n in threads:
    n.join()

from multiprocessing import Process
import time

def calculate(a):
    time.sleep(2)
    print(a)
processes_arr = []
for i in range(10):
    process = Process(target=calculate,args=(i,))
    processes_arr.append(process)
    process.start()
for n in processes_arr:
    n.join()


