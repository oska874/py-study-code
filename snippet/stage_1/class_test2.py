# abstract class

class Super:
	def acti(self):
		assert False,'not defined'

class Child(Super):
	pass

a=Child()

def mumu(self):
	print('defined acti')

Child.acti=mumu
a.acti()

# abstractmethod
from abc import ABCMeta,abstractmethod
class Super2:
	__metaclass__=ABCMeta
	@abstractmethod
	def acti2(self):
		pass

class C2(Super2):
	def acti2(self):
		print("inherit from abs")

c2 = C2();
#s2 = Super2()
		

