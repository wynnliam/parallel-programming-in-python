# To run, do "python -m scoop pi_calculus.py"

import math
from random import random
from scoop import futures
from time import time

def evaluate_points_in_circle(attempts):
	points_fallen_in_unit_circle = 0

	for i in range(0, attempts):
		x = random()
		y = random()

		radius = math.sqrt(x * x + y * y)
		if radius < 1:
			points_fallen_in_unit_circle += 1

	return points_fallen_in_unit_circle

def monte_carlo(workers, attempts):
	print("Number of workers %i - number of attempts %i" % (workers, attempts))

	bt = time()

	evaluate_task = futures.map(evaluate_points_in_circle, [attempts] * workers)
	task_result = sum(evaluate_task)

	print("%i points fallen in a unit circle after " % (task_result / attempts))

	pi_value = (4. * task_result / float(workers * attempts))

	computation_time = time() - bt

	print("Value of pi = " + str(pi_value))
	print("Error percentage = " + str(((abs(pi_value - math.pi) * 100) / math.pi)))
	print("Total time: " + str(computation_time))

for i in range(1, 4):
	monte_carlo(i * 1000, i * 1000)
	print(" ")
