import asyncio
import sys

@asyncio.coroutine
def sum_of_n_integers(future, n):
	count = 0

	for i in range(1, n + 1):
		count = count + i

	yield from asyncio.sleep(4)

	future.set_result("Sum of n integers is %s" % (count))

@asyncio.coroutine
def factorial(future, n):
	count = 1

	for i in range(2, n + 1):
		count *= i

	yield from asyncio.sleep(3)

	future.set_result("Factorial result is %s" % (count))

def got_result(future):
	print(future.result())

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

loop = asyncio.get_event_loop()
future_1 = asyncio.Future()
future_2 = asyncio.Future()

tasks = [
	sum_of_n_integers(future_1, n1),
	factorial(future_2, n2)
]

future_1.add_done_callback(got_result)
future_2.add_done_callback(got_result)

loop.run_until_complete(asyncio.wait(tasks))
loop.close()
