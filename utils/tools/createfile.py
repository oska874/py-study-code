import sys,os

# create 1m file an 512k file

ss_size = 4096
ss_num = 32
size1m = 8
size512k = 4
num1m = 8
num512k = 12
filenum = num1m + num512k
flashlen = 16*1024

# big file like 1m+
for x in range(size1m):
	print(x)
	str1 = ''
	fd = open("testfile_"+str(x),'w')
	for y in range(size1m*ss_size*ss_num/4):
		str1 += "1m%2d" % x
	fd.write(str1)
	fd.close()

# normal file , like about 512k
for x in range(num1m ,num1m+num512k):
	print(x)
	str1 = ''
	fd = open("testfile_"+str(x),'w')
	for y in range(size512k*ss_size*ss_num/8):
		str1 += "512k%4d" % x
	fd.write(str1)
	fd.close()

