from multiprocessing import Pipe

snd,rcv = Pipe()
snd.send_bytes("1234");
print (rcv.recv_bytes())
