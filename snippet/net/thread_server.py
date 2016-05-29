
import threading , time  , os , sys  , socket , traceback

def handlechild(clientsock):
    print("new child ",threading.current_thread().getName())
    print("got connection from  ",clientsock.getpeername())


    while 1:
        data = clientsock.recv(4096)
        if not len(data):
            break
        clientsock.sendall(data)
        print("recv %s"%data)
    clientsock.close()
    print("exit thread")

if __name__ == "__main__":
    host = ""
    port = 51234
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    s.bind((host,port))
    s.listen(1)

    while 1:
        try:
            clientsock , clientaddr = s.accept()
        except KeyboardInterrupt:
            break
        except:
            traceback.print_exc()
            continue

        t = threading.Thread(target= handlechild , args=[clientsock])
        t.setDaemon(1)
        t.start()

    sys.exit(0)