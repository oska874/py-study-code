import mod2
x=33
print(mod2.mod1.x)
print(mod2.x)
print(x)
mod2.mod1.x=3

print(mod2.mod1.x)
print(mod2.x)
print(x)

reload( mod2)
print(mod2.mod1.x)
print(mod2.x)
print(x)