import sqlite3
import os,sys

#read all file in current directory and store their content,size,name into bigfile.db,then read it



def getfile(name):
    fd = open(name,"rb")
    if not fd:
        print("no file")
        return None
    else:
        cont = ""
        for line in fd:
            cont += str(line)
        fd.close()
        return cont

bigtest = sqlite3.connect("bigfile.db")
bcurs = bigtest.cursor()

bcurs.execute("create table if not exists bf (filec blob ,sizec integer,fname text,fno integer primary key)")


flist = os.listdir()

no = 0
for line in flist:
    val = getfile(flist[no])
    vsize = len(val)
    tu = (val,vsize,flist[no],no,)
    tu2 = (no,)
    bcurs.execute("select ? as fno",tu2)
    if bcurs.fetchall():
        continue
    bcurs.execute("insert into bf values (?,?,?,?)",tu)
    del tu
    no += 1

bcurs.execute("select * from bf")

x = bcurs.fetchall()
if not x:
    print("empty")
else:
    for line in x:
        print(line[1],line[2],line[3])
bigtest.commit()
bigtest.close()
