try:
	a = 10
	assert(a == 9)
except Exception, e:
	print("val a not defined")
else:
	print("normal: "+str(a))
finally:
	print("finally: "+str(a))


try:
	raise IndexError
except IndexError:
	print('idx except')
finally:
	print('idx except test')

try:
	assert(a == 9)
except AssertionError:
	print("assert error")


class Bad(Exception):
	pass

def doomed():
	raise Bad()

try:
	doomed()
except Bad:
	print('got bad')


with open('acc','r') as file2:
	file2.readline()
	print("fff")