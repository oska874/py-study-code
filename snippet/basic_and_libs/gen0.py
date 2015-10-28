x=range(10)
print(x)

y=(i for i in x)

print(next(y))



z=list(y)
print(z)

print(next(y))
y=iter(y)
print(next(y))