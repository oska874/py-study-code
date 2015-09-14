def gen():
	for i in range(10):
		x=yield i
		print(x)

g=gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print(g.send(77))