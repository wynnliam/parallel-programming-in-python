import multiprocessing
import time

def foo():
	name = multiprocessing.current_process().name
	print('Starting %s\n' % name)
	time.sleep(10)
	print('Exiting %s\n' % name)

process_with_name = multiprocessing.Process(name='foo_process', target=foo)
# Will make it a background process
process_with_name.daemon = True
process_with_name.start()
