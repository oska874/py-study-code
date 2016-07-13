# -*- coding: utf-8 -*-

import socket,sys,threading,time
 
if len(sys.argv)!=4:
    print('usage:\n' , sys.argv[0] , 'dest ip' ,'thread number','package size')
    sys.exit(1)
     
ip=sys.argv[1]
tp='sendudp'
tno=int(sys.argv[2]) #has a size-resitrict
 
udpdata=b'a'*int(sys.argv[3])
 
def sendudp(host,port=449):
    to = 0
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print('Udp sending... ')
    while True:
        s.sendto(udpdata,(host,port))
        #time.sleep(0.001)
        to+=1
        if to == 0x10000:
            break
         
tlst=[]
 
for i in range(tno):
    th=threading.Thread(target=eval(tp),args=(ip,))
    tlst.append(th)
     
for i in tlst:
    i.start()