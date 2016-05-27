import fcntl , traceback , os , sys , time ,socket

def getlastaccess(fd, ip):
    fcntl.flock(fd,fcntl.LOCK_SH)

    try:
        fd.seek(0)
        for line in fd.readlines():
            filep , accesstime = line.strip().split("|")
            print(filep,accesstime)
            if filep == ip :
                return accesstime
        return None
    finally:
        fcntl.flock(fd,fcntl.LOCK_UN)

def writelastaccess(fd , ip):
    fcntl.flock(fd,fcntl.LOCK_EX)
    records = []

    try:
        fd.seek(0)
        for line in fd.readlines():
            fileip , accesstime = line.strip().split("|")
            if fileip != ip:
                records.append((fileip,accesstime))
                print(fileip, accesstime)

        fd.seek(0)

        for fileip , accesstime in records +[(ip, time.asctime())]:
            fd.write("%s|%s\n" % (fileip,accesstime))
            print(fileip,accesstime)

        fd.truncate()

    finally:
        fcntl.flock(fd,fcntl.LOCK_UN)


def reap():
    while 1:
        try:
            result = os.waitpid(-1,os.WNOHANG)
            if not result[0] :
                break
        except:
            break

        print("repead child process %d"%result[0])


if __name__ == "__main__":
    host = ''
    port = 51234

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((host,port))
    s.listen(1)

    fd=open("lastaccess.txt","w+")

    print("parent at %d listening \n"%os.getpid())

    while 1:
        try:
            clientsock, clietnaddr = s.accept()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue

        reap()

        pid = os.fork()

        if pid:
            clientsock.close()
            print("parent\n")
            continue
        else:
            print("child\n")
            s.close()

        try:
            print("got connection from %s server with pid %d\n" % (clientsock.getpeername(), os.getpid()))
            ip = clientsock.getpeername()[0]
            clientsock.sendall("welcome %s\n"%ip)
            last = getlastaccess(fd,ip)

            if last :
                clientsock.sendall('i last saw you at %s\n'%last)
            else:
                clientsock.sendall("i've never seen you before\n")

            writelastaccess(fd,ip)

            clientsock.sendall("i have noted you conn at %s\n"%getlastaccess(fd,ip))

        except (KeyboardInterrupt , SystemExit):
            raise
        except:
            traceback.print_exc()

        try:
            clientsock.close()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()

        sys.exit(0)
