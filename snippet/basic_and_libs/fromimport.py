from testfi import x,y

print(x,y)

x= 0
y=''

print(x,y)


import testfi

testfi.x=1
testfi.y='b'

print(x,y)
print(testfi.x,testfi.y)

print(testfi.__dict__)