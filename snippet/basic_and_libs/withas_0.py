
from __future__ import with_statement

with open('arc','wb+') as file1:
	print(file1.readline())

class Tbck:
	def msg(self,arg):
		print('AA: ',arg)

	def __enter__(self):
		print('start')
		return self

	def __exit__(self,exc_type,exc_val,exc_tb):
		if exc_type is None:
			print('end')
		else:
			print('end exec')
			return False

with Tbck() as act:
	act.msg('ttt')
	print('reached')

print('\n\n')

with Tbck() as act2:
	act2.msg('test 2 ')
	raise TypeError
	print('not reached')