import serial
import serial.tools.list_ports
import io
import time
from xmodem import XMODEM

"""
两个关键点：
1. 识别、打开、读写串口，可以发送命令
2. 使用 xmodem 协议传输数据，可以传送文件
以此为基础，实现通过串口操纵开发板
"""

breaked = 0
FILE1 = "D:\\code\\py-study-code\\snippet\\sqlite\mac.txt"
fr = ""

def getc(size, timeout=1):
    return main_ser.read(size) or None

def putc(data, timeout=1):
    return main_ser.write(data)

with serial.Serial("com6",115200,timeout=5) as main_ser:
    print("stag 1")
    print(main_ser)
    print(main_ser.is_open)
    modem = XMODEM(getc, putc)
    while(1):
        line = main_ser.readline()
        if breaked == 0 :
            main_ser.write(b'\n')
            breaked=1
        print(line)
        if b'autoboot Hit any key to stop autoboot:' in line:
            break

    print("stag 2")
    while(1):
        line = main_ser.readline()
        if b'=> ' in line:
            break
    print(line)
    if b'=> ' in line:
        print(line)#just for debug
        main_ser.write(b'loadx 0x1000000\n\n')#send comand
        time.sleep(0.1)
        line = main_ser.readline()#get the output of the upper command
        print(line)
        line = main_ser.readline()
        print(line)
        print("send data")
        f1 = open(FILE1,"rb") #send opened file to board via xmodem
        modem.send(f1)
        print("sended")
    else:
        print("error1")
    while (1):
        line = main_ser.readline()
        if b'=> ' in line:
            break
    print(line)
    if b'=> ' in line:
        print("a1")
        #main_ser.write(b"md 0x1000000;\n\n")
        #main_ser.readline()
        #burn to flash
        #main_ser.write(b"protect off all;erase 0xef040000 +0xc0000;cp.b 0x01000000 0xef040000 0xc0000;\n\n")
        #program mac addr
        #main_ser.write(b"pro off all;erase 0xec020000 +0x20000;")
    else:
        print("error2")





