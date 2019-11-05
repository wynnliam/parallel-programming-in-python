import concurrent.futures
import time

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def evaluate_item(x):
	result = count(x)
	print("item " + str(x) + " result: " + str(result))

def count(number):
	for i in range(0, 10000000):
		i = i + 1
	return i * number

# Evaluate sequentially
start_time = time.clock()

for item in number_list:
	evaluate_item(item)

print("Sequential execution in " + \
	  str(time.clock() - start_time) + " seconds")


# Evaluate with thread pool execution
start_time = time.clock()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
	for item in number_list:
		executor.submit(evaluate_item, item)

print("Thread pool execution in " + \
	  str(time.clock() - start_time) + " seconds")


# Evaluate with process pool execution
start_time = time.clock()

with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
	for item in number_list:
		executor.submit(evaluate_item, item)

print("Process pool execution in " + \
	  str(time.clock() - start_time) + " seconds")
