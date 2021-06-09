#! /usr/bin/python3
import threading
import time
# Thread.start() :- Start Function start multiple threads at one time
# Thread.run() :- Start Function start one threads at one time

ls = []


def count(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.5)
        print("x{}".format(i))
def count2(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.5)
        print("y{}".format(i))
        

x = threading.Thread(target=count,args=(10,))
x.start()
x.join()

y = threading.Thread(target=count2,args=(10,))
y.start()
y.join()

print(ls)