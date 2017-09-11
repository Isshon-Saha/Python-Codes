import threading
import time

def func(num1,num2):
     print("Hello world")
     time.sleep(1)

threads=[]
for i in range(5):
    t=threading.Thread(target=func(2,3))
    threads.append(t)
    t.start()