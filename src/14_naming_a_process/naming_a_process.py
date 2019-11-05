import multiprocessing
import time

def foo():
	name = multiprocessing.current_process().name
	print('Starting %s\n' % name)
	time.sleep(3)
	print('Exiting %s\n' % name)

process_with_name = multiprocessing.Process(name='foo_process', target=foo)
process_with_name.start()
process_with_name.join()
