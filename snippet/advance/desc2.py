# -*- encoding:utf8 -*-

class Desc(object):
    def __init__(self,value):
        print("init")
        self.value=value
    def __set__(self,instance,value):
        print("set")
        self.value=value*10
    def __get__(self,instance,owner):
        print("get")
        return self.value

class Desc2(object):
    def __set__(self,instance,value):
        print("set2")
        instance._y=value
    def __get__(self,instance,owner):
        print("get2")
        return instance._y*100


class Calc(object):
    x = Desc(2)
    y = Desc2() 
    def __init__(self):
        self.z = 4
        print("1")
        self._y = 3
        print("2")


print("a")
obj = Calc()
print("b")

print(obj.x,obj.y,obj.z)
print("c")


obj.x=4
obj.y=5
obj.z=6

print(obj.x,obj.y,obj.z)

