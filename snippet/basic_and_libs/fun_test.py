from print30 import print30

def fun_lc(fun,para):
	fun(para)
	print("fun vars: " + str(fun_lc.count))

ff=fun_lc

ff.count=4
print(ff.count)

def xx(para):
	print(para)

fun_lc(print30,"456")

print(fun_lc.__class__)
print(dir(fun_lc))

print('\n\n')

def f1():
	ac=(lambda x:x)
	return ac

x2=f1()
print(x2('jjj'))
