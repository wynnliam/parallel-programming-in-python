import multiprocessing

def worker(dictionary, key, item):
	dictionary[key] = item

mgr = multiprocessing.Manager()
dictionary = mgr.dict()
jobs = [multiprocessing.Process(target=worker, args=(dictionary, i, i * 2)) \
	    for i in range(10)]

for j in jobs:
	j.start()
for j in jobs:
	j.join()

print('Results:', dictionary)
