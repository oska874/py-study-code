import threading , time

def singleti(num):
    print(num)
    xx = threading.local()
    xx.x = num
    print(xx.x)
    if num == 'xx':
        print("daemon")
        time.sleep(1)
        print("ooo")


th0 = threading.Thread(target=singleti,name="ss",args=("xx",))
th1 = threading.Thread(target=singleti,name="dd",args=("yy",))
th2 = threading.Thread(target=singleti,name="cc",args=("zz",))

th0.setDaemon(1)

th0.start()
th1.start()
th2.start()


th1.join()
th2.join()
th0.join()
print("end")
