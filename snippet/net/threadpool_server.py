
import sys,os,threading,traceback,time,socket


def handkecinnection(clientsock):
    lockpool.acquire()
    print("recv new client conn")
    try:
        if len(waitinglist) == 0 and (threading.activeCount() - 1)>= MAXTHREAD:
            clientsock.close()
            return
        if len(waitinglist) == 0:
            startthread()

        queue.append(clientsock)
        sem.release()
    finally:
        lockpool.release()

def startthread():
    print("start new client processor thread")
    t = threading.Thread(target=threadworker)
    t.setDaemon(1)
    t.start()

def threadworker():
    global waitinglist,lockpool,busylist
    time.sleep(1)
    name = threading.currentThread().getName()

    try:
        lockpool.acquire()
        try:
            waitinglist[name]=1
        finally:
            lockpool.release()
        processclients()
    finally:
        print("thread %s died"%name)
        if name in waitinglist:
            del waitinglist[name]

        if name in busylist:
            del busylist[name]

        startthread()

def processclients():
    global sem,queue,waitinglist,busylist,lockpool
    name = threading.currentThread().getName()
    while 1:
        sem.acquire()
        lockpool.acquire()

        try:
            clientsock = queue.pop(0)
            del waitinglist[name]
            busylist[name] = 1
        finally:
            lockpool.release()

        try:
            print("got connection from ",clientsock.getpeername())
            clientsock.sendall("greetings . you are being served by %s\n"%name)
            while 1:
                data = clientsock.recv(4096)
                if data.startswith('DIE'):
                    sys.exit(0)
                if not len(data):
                    break
                clientsock.sendall(data)
        except(KeyboardInterrupt,SystemExit):
            raise
        except:
            traceback.print_exc()

        try:
            clientsock.close()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()

        lockpool.acquire()

        try:
            del busylist[name]
            waitinglist[name] = 1
        finally:
            lockpool.release()


def listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
    s.bind((host,port))
    s.listen(1)

    while 1:
        try:
            clientsock, clientaddr = s.accept()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue

        handkecinnection(clientsock)


if __name__ == "__main__":
    host = ''
    port = 51234
    MAXTHREAD = 3
    lockpool = threading.Lock()
    busylist = {}
    waitinglist = {}
    queue = []
    sem = threading.Semaphore(0)

    listener()