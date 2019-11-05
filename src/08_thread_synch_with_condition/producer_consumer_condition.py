from threading import Thread, Condition
import time

items = []
condition = Condition()

class consumer(Thread):
	def __init__(self):
		Thread.__init__(self)

	def consume(self):
		global condition
		global items

		condition.acquire()

		if len(items) == 0:
			condition.wait()
			print("Consumer notify : no item to consume")

		items.pop()

		print("Consumer notify : consumed 1 item")
		print("Consumer notify: items to consume are " + str(len(items)))

		condition.notify()
		condition.release()

	def run(self):
		for i in range(20):
			time.sleep(1)
			self.consume()

class producer(Thread):
	def __init__(self):
		Thread.__init__(self)

	def produce(self):
		global condition
		global items

		condition.acquire()

		if len(items) == 10:
			condition.wait()

			print("Producer notify : items produced are " + str(len(items)))
			print("Producer notify : stop the production!")

		items.append(1)
		print("Producer notify : total items produced " + str(len(items)))

		condition.notify()
		condition.release()

	def run(self):
		for i in range(20):
			time.sleep(2)
			self.produce()

p = producer()
c = consumer()

p.start()
c.start()

p.join()
c.join()
