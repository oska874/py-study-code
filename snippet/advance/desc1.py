
class Name(object):
    def __set__(self,instance,value):
        print("set")
        instance._name=value
    def __get__(self,instance,owner):
        return instance._name

class Person(object):
    def __init__(self,name):
        print("init")
        self._name=name
    name = Name()


bob = Person("fdfad")
print(bob.name)
bob.name = "13213"
print(bob.name)
