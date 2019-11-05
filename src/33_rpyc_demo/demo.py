# To run:
# First run "python /bin/rpyc_classic.py"
# Then run "python demo.py"

import rpyc
import sys

c = rpyc.classic.connect("localhost")
c.execute("print ('hi')")
c.modules.sys.stdout = sys.stdout
c.execute("print ('hi 2')")
