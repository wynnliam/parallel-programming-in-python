import Pyro4

class Account(object):
	def __init__(self):
		self._balance = 0.0

	def pay(self, price):
		self._balance -= price

	def deposit(self, cash):
		self._balance += cash

	def balance(self):
		return self._balance

class Shop(object):
	def __init__(self):
		self.accounts = { }
		self.clients = []

	@Pyro4.expose
	def name(self):
		return 'Cool Shop'

	@Pyro4.expose
	def log_on(self, name):
		if name in self.clients:
			self.accounts[name] = Account()
		else:
			self.clients.append(name)
			self.accounts[name] = Account()

	@Pyro4.expose
	def deposit(self, name, amount):
		try:
			return self.accounts[name].deposit(amount)
		except KeyError:
			raise KeyError('unknown account!')

	@Pyro4.expose
	def balance(self, name):
		try:
			return self.accounts[name].balance()
		except KeyError:
			raise KeyError('unknown account')

	@Pyro4.expose
	def allAccounts(self):
		accs = { }

		for name in self.accounts.keys():
			accs[name] = self.accounts[name].balance()

		return accs

	@Pyro4.expose
	def buy(self, name, price):
		balance = self.accounts[name].balance()
		self.accounts[name].pay(price)
