from multiprocessing import Queue

q0 = Queue(100)

q0.put((1,"1",(1),("1")))

print(q0.get())

q0.put([1,"1",[1],{"1":1}])

print(q0.get())
