def prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    for i in range(2,x):
        if x % i == 0:
            return False            
    return True

for i in range(1,100):
    print(i,prime(i))
