
import socket,sys,time,threading

def fwrite(buf):
    sys.stdout.write(buf)
    sys.stdout.flush()

def spin():
    global spinpos
    fwrite(spinners[spinpos]+'\b')
    spinpos += 1
    if spinpos >= len(spinners):
        spinpos = 0

def uithread():
    while 1:
        cv.acquire()
        while not len(equeue):
            cv.wait(0.15)
            spin()

        msg =equeue.pop(0)
        cv.release()

        if msg == 'QUIT':
            fwrite('\n')
            sys.exit(0)
        fwrite(' \n %s\r' % msg)

def msg(message):
    cv.acquire()
    equeue.append(message)
    cv.notify()
    cv.release()

if __name__ == "__main__":
    host = sys.argv[1]
    textport = sys.argv[2]
    filename = sys.argv[3]
    cv = threading.Condition()
    spinners = '|/-\\'
    spinpos = 0
    equeue = []

    t = threading.Thread(target= uithread)
    t.setDaemon(1)
    t.start()

    try:
        msg('creating socket object')
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error,e:
        print('error create socket')
        sys.exit(1)

    try:
        port = int(textport)
    except ValueError:
        try:
            port = socket.getservbyname(textport, 'tcp')
        except socket.error, e:
            print("cannot find your port %s"%e)
            sys.exit(1)
    msg("connecting to %s:%d"%(host,port))
    time.sleep(4)

    try:
        s.connect((host,port))
    except socket.gaierror, e:
        print("address-related err connect to server %s"%e)
        sys.exit(1)
    except socket.error, e:
        print("connection error %s"%e)
        sys.exit(1)

    msg('sending query')
    time.sleep(5)
    try:
        s.sendall("get %s"%filename)
    except socket.error, e:
        print("error sending %s"%e)
        sys.exit(1)

    msg("shutting down socket")
    time.sleep(3)
    try:
        s.shutdown(1)
    except socket.error, e:
        print("shutdown %s"%e)
        sys.exit(1)

    msg('recv data')
    count = 0
    while 1:
        try :
            buf = s.recv(2048)
        except socket.error, e:
            print("error recv %s"%e)
            sys.exit(1)

        if not len(buf):
            break
        count += len(buf)

    msg ("recv %d bytes"%count)
    msg ("QUIT")
    t.join()
