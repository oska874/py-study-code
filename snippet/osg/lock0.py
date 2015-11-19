import threading

some_rlock = threading.RLock()

with some_rlock:
    print("some locking")
