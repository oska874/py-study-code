# -*- encoding:utf-8 -*-

class Desc(object):
    def __get__ (self,instance,owner):
        print("get")
        print(self,instance,owner)
        return instance._attr

    def __set__(self,instance,value):
        print("set")
        instance._attr = value

class Subj(object):
    def __init__(self,atr):
        self._attr=atr
#    attr=Desc()


x = Subj("1234")
print(x._attr)

x.attr="999"
print(x._attr)

