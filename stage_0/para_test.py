# -*- coding: utf-8 -*

az=10
def azt():
	global az
	az =11
	print(az)

azt()
print(az)

def azt2():
	import __main__
	print(__main__.az)
	az = 10
	print(az)

azt2()
print(az)


"""
# fault usage
def a1(a,b=1,c,d=2):
"""
def a1(a,b,c=0,d=1):
	print(a)
	print(b)
	print(c)
	print(d)

a=0
a1(1,2,3)
a1(2,3,4,5)

print('keyword-')
a1(b=0,a=1,d=3,c=4)


def var_fun(*a):
	for x in a:
		print(x)

var_fun(1,2,3,4,5,6788)
var_fun(1)

bb=[1,2,3,4,5,6]
var_fun(bb)
var_fun(*bb)

def dict_fun(jj):
	for ij in jj:
		print(ij)
		print(jj[ij])

dict_fun({'1':'2','a':'b'})

def dict_fun2(**jj):
	for ij in jj:
		print(ij)
		print(jj[ij])
print('dict')
dict_fun(jj={'1':'2','a':'b'})


def mix_fun(a,b,c=1,*d,**e):
	print(a)

	print(b)

	for x in c:
		print(x)

	for x in d:
		print(x)

print('mix use')

mix_fun(1,['1','b','c','d'],
	*('a','b','c','d'),**{'e':'f'})


def star2_fun(**args):
	print(args)

star2_fun()
star2_fun(a=1,b=2,c=3)


def echo1(*args,**kwargs):
	print(args,kwargs)

echo1(1,b=4) #** 只对关键字有效

pargs=(1,2)
kargs={'a':3,'b':4}
apply(echo1,pargs,kargs)



def ddd(a=[]):
	a.append(1)
	print(a)
	return a

sa = [1,2]
print(ddd())
print(ddd())
print(ddd())
print(ddd())
print(ddd())
print(ddd())
print(ddd())