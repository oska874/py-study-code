

def func():
    pass
func.temp =1
print(func.__dict__)

class TempClass(object):
    a = 1
    def tempFunction(self):
        pass

print( TempClass.__dict__)