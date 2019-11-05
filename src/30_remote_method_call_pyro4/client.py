# To run:
# First, open a terminal and run 'python -m Pyro4.naming'
# Next, open another terminal and run 'python server.py'
# Then, open a third terminal and run 'python client.py'

import Pyro4

#uri = input("Insert the PYRO4 server URI (help: PYRONAME:server) ").strip()
name = input("What is your name? ").strip()

server = Pyro4.Proxy("PYRONAME:server")
print(server.welcome(name))
