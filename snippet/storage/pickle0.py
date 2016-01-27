import pickle

class Foo:
    attr = 'a class attr'

picklestring = pickle.dumps(Foo)
print(picklestring)
