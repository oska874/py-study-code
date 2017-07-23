#used in python 2.7
#in python 3 ,rename copy_reg to copyreg
import copy_reg, copy, pickle
class C(object):
    def __init__(self, a):
        self.a = a
def pickle_c(c):
    print("pickling a C instance...")
    return C, (c.a,)

copy_reg.pickle(C, pickle_c)

c = C(1)
d = copy.copy(c)
p = pickle.dumps(c)
