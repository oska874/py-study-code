# -*- coding: utf-8 -*- 

#tar

import tarfile
import sys

print(sys.getfilesystemencoding())
print(tarfile.DEFAULT_FORMAT,tarfile.GNU_FORMAT)


tar3 = tarfile.open('rrr.tar.gz','r')
print(tar3.name)
tar3.extractall()
tar3.close()

tar3 = tarfile.open('rrr.tar','w')
tar3.add('rrr')
tar3.close()

istar=tarfile.is_tarfile('rrr.tar')

if istar == True:
	tar1 = tarfile.open('rrr.tar','r')
else:
	exit()

tar1.extractall()
tar1.extract(tar1.getmember('rrr'))
tar1.close()

#compress,package
tar2 = tarfile.open("sample.tar","w")
tar2.add('rrr')
tar2.add('rrr1.gz')
tar2.close()

#read gzip

istar = tarfile.is_tarfile('rrr1.gz')
print("is rrr1.gz is tar "+str(istar))
tar3 = tarfile.open("rrr1.gz.tar","w")
tar3.add('rrr1.gz')
tar3.close()

print("test end 1")

def reset(ti):
	ti.uid = ti.git = 0
	ti.uname = ti.gname = "root"
	return ti

tar3 = tarfile.open("test.tar.gz",'w:gz')
tar3.add('rrr',filter=reset)
tar3.close()

print("test end 2")


