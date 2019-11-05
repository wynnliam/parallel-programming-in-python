import operator
import time

from scoop import futures

def simulated_workload(input_data):
	time.sleep(0.01)
	return sum(input_data)

def compare_map_reduce():
	data = list([a] * a for a in range(1000))

	map_scoop_time = time.time()
	result = futures.mapReduce(simulated_workload, operator.add, data)
	map_scoop_time = time.time() - map_scoop_time
	print('futures.map in SCOOP executed in {0:.3f}s with result: {1}'.format(map_scoop_time, result))

	map_python_time = time.time()
	result = sum(map(simulated_workload, data))
	map_python_time = time.time() - map_python_time
	print('map Python executed in {0:.3f}s with result: {1}'.format(map_python_time, result))

if __name__ == '__main__':
	compare_map_reduce()
