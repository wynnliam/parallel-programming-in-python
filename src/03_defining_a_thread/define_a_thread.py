import threading
from time import sleep

def my_function(i):
	for j in range(3):
		print("Function called by thread ", i, "\n")
		sleep(1)

threads = []

for i in range(5):
	# note that we need the , in the args tuple otherwise we get
	# some ugly errors.
	t = threading.Thread(target=my_function, args=(i,))
	threads.append(t)
	# This will actually start the thread
	t.start()
	# This will force the main thread to wait until the called thread
	# is done. Comment this out and see how the behavior changes
	t.join()
