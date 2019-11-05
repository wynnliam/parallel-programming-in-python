import threading
import time

def thread_function():
	name = threading.currentThread().getName()
	print(name + ' is starting\n')
	time.sleep(2)
	print(name + ' is exiting\n')

# for i in range(5):
# 	t = threading.Thread(name=str(i), target=thread_function)
# 	t.start()
# 	#t.join()

t1 = threading.Thread(name='Function 1', target=thread_function)
t2 = threading.Thread(target=thread_function)

t1.start()
t2.start()

t1.join()
t2.join()
