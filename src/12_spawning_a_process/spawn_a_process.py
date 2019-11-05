import multiprocessing
import time

def function(i):
	print('Called function in process %s' % i)
	time.sleep(10)

process_jobs = []

for i in range(5):
	p = multiprocessing.Process(target=function, args=(i,))
	process_jobs.append(p)
	p.start()
	p.join()
