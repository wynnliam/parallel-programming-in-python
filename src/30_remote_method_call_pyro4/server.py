import Pyro4

class Server(object):
	@Pyro4.expose
	def welcome(self, name):
		return "Welcome, " + str(name)

def start_server():
	server = Server()
	daemon = Pyro4.Daemon()

	# Locate name server running
	ns = Pyro4.locateNS()

	# Register server as a Pyro object
	uri = daemon.register(server)

	# Register the object with a name in the name server
	ns.register("server", uri)

	# Print the URI so we can use it in the client later
	print("Ready. Object uri = ", uri)

	daemon.requestLoop()

if __name__ == "__main__":
	start_server()
