
import sys, socket

if __name__ == "__main__":
    s = socket.getaddrinfo("baidu.com",80)
    for x in s:
        print(x)

    s = socket.getnameinfo(("111.13.101.208",80),1)
    print(s)
