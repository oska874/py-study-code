import threading

def singleti(num):
    print(num)
    xx = threading.local()
    xx.x = num
    print(xx.x)

th0 = threading.Thread(target=singleti,name="ss",args=("xx",))
th1 = threading.Thread(target=singleti,name="dd",args=("yy",))

th0.start()
th1.start()
