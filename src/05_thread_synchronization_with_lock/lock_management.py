import threading

COUNT = 100000

shared_resource_with_lock  = 0
shared_resource_with_no_lock = 0

shared_resource_lock = threading.Lock()

def increment_with_lock():
	global shared_resource_with_lock
	for i in range(COUNT):
		shared_resource_lock.acquire()
		shared_resource_with_lock += 1
		shared_resource_lock.release()

def decrement_with_lock():
	global shared_resource_with_lock
	for i in range(COUNT):
		shared_resource_lock.acquire()
		shared_resource_with_lock -= 1
		shared_resource_lock.release()

def increment_without_lock():
	global shared_resource_with_no_lock
	for i in range(COUNT):
		shared_resource_with_no_lock += 1

def decrement_without_lock():
	global shared_resource_with_no_lock
	for i in range(COUNT):
		shared_resource_with_no_lock -= 1

# LOCK MANAGEMENT DEMO
t1 = threading.Thread(target=increment_with_lock)
t2 = threading.Thread(target=decrement_with_lock)

t1.start()
t2.start()

t1.join()
t2.join()

print('The value of the resource with lock management is ', shared_resource_with_lock)

# WITHOUT LOCK MANAGEMENT DEMO
t3 = threading.Thread(target=increment_without_lock)
t4 = threading.Thread(target=decrement_without_lock)

t3.start()
t4.start()

t3.join()
t4.join()

print('The value of the resouce without lock management is ', shared_resource_with_no_lock)
