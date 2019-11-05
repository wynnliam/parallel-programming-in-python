from __future__ import print_function
import Pyro4

class Chain(object):
	def __init__(self, name, next_name):
		self.name = name
		self.next_name = next_name
		self.next = None

	@Pyro4.expose
	def process(self, message):
		if self.next is None:
			self.next = Pyro4.core.Proxy("PYRONAME:example.chain_topology." + self.next_name)

		if self.name in message:
			print("Back at %s; chain is closed!" % self.name)
			return ["complete at " + self.name]
		else:
			print("%s forwarding the message to the object %s" % (self.name, self.next_name))
			message.append(self.name)

			result = self.next.process(message)
			result.insert(0, "passed on from " + self.name)

			return result

