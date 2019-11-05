from threading import Thread
from time import sleep

class CookBook(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.message = "Hello from CookBook!\n"

	def print_message(self):
		print(self.message)

	def run(self):
		print("Thread starting\n")
		x = 0
		while x < 10:
			self.print_message()
			sleep(2)
			x += 1

		print("Thread ended\n")

print("Process started")

cook_book = CookBook()
cook_book.start()

print("Process ended")
