# -*- coding:utf-8 -*-
import sqlite3
import struct
import pickle
import codecs
import unicodedata

#original data form this file
macsrc = open("macs2.txt","rb")
#create the database
conn = sqlite3.connect('macs.db')
c = conn.cursor()
c.execute("""create table if not exists macs 
                (val text primary key , used INTEGER)""")
#insert data into db
try:
    while 1:
        line = macsrc.readline()
        #print(line)
        if not line:
            break
        tu = (line,)
        c.execute("select * from macs where val=?",tu)
        if not c.fetchall():
            c.execute("""insert into macs values
                (?,0)""",tu)
        del tu
except sqlite3.IntegrityError:
    pass
conn.commit()
conn.close()

#print data in db
conn = sqlite3.connect('macs.db')
c = conn.cursor()
c.execute("select * from macs")
print("-----")
print(c.fetchall())




