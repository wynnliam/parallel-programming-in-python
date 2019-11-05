from __future__ import print_function
import Pyro4

obj = Pyro4.core.Proxy("PYRONAME:example.chain_topology.1")
print("Result = %s" % obj.process(["hello"]))
