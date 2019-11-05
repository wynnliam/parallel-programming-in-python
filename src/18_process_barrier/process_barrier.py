import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
	name = multiprocessing.current_process().name
	synchronizer.wait()

	now = time()

	with serializer:
		print("Process %s ----> %s" % (name, datetime.fromtimestamp(now)))

def test_without_barrier():
	name = multiprocessing.current_process().name
	now = time()
	print("Process %s ----> %s" % (name, datetime.fromtimestamp(now)))

synchronizer = Barrier(2)
serializer = Lock()
Process(name="p1 - test with barrier", target=test_with_barrier, args=(synchronizer, serializer)).start()
Process(name="p2 - test with barrier", target=test_with_barrier, args=(synchronizer, serializer)).start()
Process(name="p3 - test without barrier", target=test_without_barrier).start()
Process(name="p4 - test without barrier", target=test_without_barrier).start()
