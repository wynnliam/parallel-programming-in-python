import multiprocessing
import target

process_jobs = []

for i in range(5):
	p = multiprocessing.Process(target=target.target_function, args=(i,))
	process_jobs.append(p)
	p.start()
	p.join()
