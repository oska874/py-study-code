s1='abcd'
s2='1234'
l1=list(zip(s1,s2))
print(l1)

for x,y in zip(s1,s2):
	print(x,y)


def mymap(func,*args):
	res = []
	for x in zip(*args):
		res.append(func(*x))
	return res
	
print(mymap(abs,[1,2,3,4,5,6]))	
print(mymap(pow,[1,2,3],[2,3]))

print("return")
def mymap2(func,*args):
	return  [func(*x) for x in zip(*args)
]
print(mymap2(pow,[1,2],[2,3]))

print('yield')
def mymap3(func,*args):
	for x in zip(*args):
		yield func(*x)

print(next(mymap3(abs,[-1,-2,-3])))

print(list(mymap3(abs,[-1,-2,-3])))

print('gens')
def mymap4(func,*args):
	return (func(*x) for x in zip(*args))

print(next(mymap4(abs,[-1,-2,-3]))

)

print('myzip')

def myzip(*args):
	seq=[list(s) for s in args]
	res=[]
	while all(seq):
		res.append(tuple(s.pop(0) for s in seq))
	return res


print(list(myzip('123','abc')))

print('mymap5')

'''
#3.0
def mymap5(*args, pad=None):
	seq=[list(s) for s in args]
	res = []
	while any(seq):
		res.append(tuple((s.pop(0) if s else pad) for s in seq))
	return res

print(mymap5('1236','abc',pad=99))
'''


def mymap5(*args):
	seq=[list(s) for s in args]
	res = []
	while any(seq):
		res.append(list((s.pop(0) if s else '%') for s in seq))
	return res

print(mymap5('1236','abc'))

print('myzip1')
def myzip1(*args):
	iters=map(iter,args)
	while iters:
		res = [next(u) for u in iters]
		yield tuple(res)

print(list(myzip1('1234','abcd')))
print(list(myzip1('1234','abcd')))

ss=['abcd','efg']
print(list(map(iter,ss)[1]))



help(map)