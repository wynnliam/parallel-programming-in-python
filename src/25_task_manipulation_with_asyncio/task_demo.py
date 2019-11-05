import asyncio

@asyncio.coroutine
def factorial(num):
	f = 1
	for i in range(2, num + 1):
		print("Asyncio.Task: Compute factorial(%s)" % (i))
		yield from asyncio.sleep(1)
		f *= i

	return str("Asyncio.Task - factorial(%s) = %s" % (num, f))

@asyncio.coroutine
def fibonacci(num):
	a, b = 0, 1

	for i in range(num):
		print("Asyncio.Task: Compute fibonacci(%s)" % (i))
		yield from asyncio.sleep(1)
		a, b = b, a + b

	return str("Asyncio.Task - fibonacci(%s) = %s" % (num, a))

@asyncio.coroutine
def binomialCoeff(n, k):
	result = 1

	for i in range(1, k + 1):
		result = result * (n - i + 1) / i

		print("Asyncio.Task: Compute binom coeff(%s)" % (i))
		yield from asyncio.sleep(1)

	return str("Asyncio.Task - binomialCoeff(%s, %s) = %s" % (n, k, result))

tasks = [asyncio.Task(factorial(10)),
		 asyncio.Task(fibonacci(10)),
		 asyncio.Task(binomialCoeff(20, 10))]

loop = asyncio.get_event_loop()
result = loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# TODO: Figure out how to get the result of each function
print(result)
