
class Vars:
	x=13
	def fun1(self,xx):
		x=14
		print(x)
		print(self.x)
		print(Vars.x)

v1 = Vars()
v2 = Vars()
v1.fun1(1)
print('\n')
v1.x=99
v1.fun1(1)
print('\n')
v2.fun1(2)