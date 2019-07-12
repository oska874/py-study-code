
def test1(start,end):
    while start<end:
        yield start
        start += 1

for i in test1(0,5):
    print(i)

s = test1(10,20)

print(next(s))
print(next(s))
print(next(s))