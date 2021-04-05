import threading
import time

a = 1

def func1():
	global a
	while True:
		print("1====>  ",a)
		a+=1
		time.sleep(1)
def func2():
	global a
	while True:
		print("2====>  ",a)
		a+=1
		time.sleep(1)

th1 = threading.Thread(target=func1, args=())

th2 = threading.Thread(target=func2, args=())
th1.start()
th2.start()
