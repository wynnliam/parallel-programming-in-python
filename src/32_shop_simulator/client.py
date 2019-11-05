from __future__ import print_function
import sys
import Pyro4

ns = Pyro4.locateNS()
uri = ns.lookup('example.shop.Shop')

shop = Pyro4.core.Proxy(uri)

print('Shop: %s' % shop.name())

print('Loggin on')
shop.log_on('Squanto')

print('Adding 1000 buck to Squantos account')
shop.deposit('Squanto', 1000)

print('Buying something')
shop.buy('Squanto', 10)

print(shop.allAccounts())
