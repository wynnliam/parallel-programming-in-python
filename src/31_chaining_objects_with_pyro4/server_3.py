from __future__ import print_function

import Pyro4
import chain_topology
import Pyro4.naming

this_id = "3"
next_id = "1"

server_name = "example.chain_topology." + this_id

daemon = Pyro4.core.Daemon()
obj = chain_topology.Chain(this_id, next_id)
uri = daemon.register(obj)
ns = Pyro4.naming.locateNS()
ns.register(server_name, uri)

print("Server_%s started" % this_id)
daemon.requestLoop()


