import multiprocessing

def square(data):
	return data * data

inputs = list(range(0, 100))
pool = multiprocessing.Pool(processes=4)
pool_outputs = pool.map(square, inputs)

pool.close()
pool.join()

print('Pool		:', pool_outputs)
