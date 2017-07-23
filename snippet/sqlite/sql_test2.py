# -*- coding:utf-8 -*-
import sqlite3
import struct
import pickle
import codecs
import unicodedata

#original data form this file
macsrc = open("macs2.txt","rb")
sersrc = open("allserial.txt","rb")
#create the database
conn = sqlite3.connect('macs2.db')
c = conn.cursor()
c.execute("""create table if not exists macs 
                (val text primary key , sno text , used INTEGER)""")
#insert data into db
try:
    while 1:
        line = macsrc.readline()
        line2 = sersrc.readline()
        #print(line,line2)
        if not line or not line2:
            break
        tu = (line,)
        c.execute("select * from macs where val=?",tu)
        res = c.fetchone()
        if not res:
            tu = (line,line2,)
            c.execute("""insert into macs values
                (?,?,0)""",tu)
        else:
            pass#print("|",res)
        del tu
except sqlite3.IntegrityError:
    print("_",tu)
    pass
conn.commit()
conn.close()
print("created")
#print data in db
conn = sqlite3.connect('macs2.db')
c = conn.cursor()
c.execute("select * from macs")
while 1:
    res = c.fetchone()
    if not res:
        break
    print(res)
print("done")
conn.close()

conn = sqlite3.connect("macs2.db")
c = conn.cursor()

#set used=1 if sno is used(in allserial2.txt)
sersrc2 = open("allserial2.txt","rb")
while 1:
    sno = sersrc2.readline()
    if not sno:
        break
    tu2 = (sno,)
    c.execute("select * from macs where sno=?",tu2)
    res = c.fetchone()
    if not res:
        print("sno fault")
    else:
        c.execute("update macs set used=1 where sno=?",tu2)
        c.execute("select * from macs")
    del tu2
print("DONE1.5")
for row in c.execute("select * from macs"):
    print(row)
print("DONE2")
conn.close()






