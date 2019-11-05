import threading
import time

class Box(object):
	lock = threading.RLock()

	def __init__(self):
		self.total_items = 0

	def execute(self, n):
		Box.lock.acquire()
		self.total_items += n
		Box.lock.release()

	def add(self):
		Box.lock.acquire()
		self.execute(1)
		Box.lock.release()

	def remove(self):
		Box.lock.acquire()
		self.execute(-1)
		Box.lock.release()

# Run these functions in seperate threads
# and call the Box's methods

def adder(box, items):
	while items > 0:
		print("Adding 1 item in the box\n")
		box.add()
		time.sleep(2)
		items -= 1

def remover(box, items):
	while items > 0:
		print("Removing 1 item from the box\n")
		box.remove()
		time.sleep(2)
		items -= 1


items = 5
box = Box()

print('Putting %s items in the box' % items)

t1 = threading.Thread(target=adder, args=(box, items))
t2 = threading.Thread(target=remover, args=(box, items))

t1.start()
t2.start()

t1.join()
t2.join()

print('%s items still remain in the box' % box.total_items)
