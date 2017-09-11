import threading
import time
import kivy

i=1

def default():
    global i
    threading.current_thread().setName("Thread no. {}".format(i))
    i+=1
    print("{} starting".format(threading.current_thread().getName()))
    time.sleep(1)
    print("{} exiting".format(threading.current_thread().getName()))
    time.sleep(2)

def main():
    for j in range(5):
        w=threading.Thread(target=default())
        w.start()


if __name__ == '__main__':main()