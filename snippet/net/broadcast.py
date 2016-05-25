import  sys , socket , traceback

if __name__ == "__main__":
    type = sys.argv[1]

    if type == 'recv':
        host = ''
        port = 12345

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

        s.bind((host,port))

        while 1:
            try:
                msg, addr = s.recvfrom(4019)
                print("got data from %s"%addr[0])
                s.sendto("i am here",addr)
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                traceback.print_exc()
    elif type == 'send':
        dest = ('<broadcast>',12345)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
        s.sendto("hello",dest)

        while 1:
            buf, addr = s.recvfrom(2048)
            if not len(buf):
                break
            print("got %s"%buf)
            s.sendto("hello", dest)





