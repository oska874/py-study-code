# -*- coding: utf-8 -*-

class Person(object):
    """需要继承object"""
    def __init__(self,name):
        self._name=name
    
    @property
    def name(self):
        print('fetch ...')
        return self._name

    @name.setter
    def name(self,value):
        print("change ...")
        self._name = value

    @name.deleter
    def name(self):
        print("remove")
        del self._name


bob = Person("boc")
print(bob.name)
bob.name="jack"
print(bob.name)
del bob.name
