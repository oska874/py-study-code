# -*- coding: utf-8 -*- 

#zip
import zipfile

z1 = zipfile.ZipFile("test.zip",'w',zipfile.ZIP_DEFLATED,)
z1.write("file.txt.gz")
z1.write("test2.tar")
z1.write('rrr')
z1.close()

z1 = zipfile.ZipFile('test.zip','r')
zi = z1.getinfo('file.txt.gz')
print(zi)
znames = z1.namelist()
print(znames)
zr = z1.open('rrr')
for x in zr:
	print(x)

z1.extract('rrr')
z1.printdir()
z1.close()

z2 = zipfile.ZipFile("test2.zip",'w')

z2.writestr("test2","12345678")
print("zip comment")
#z2.comment("hello world")	#how?
z2.close()

z0 = zipfile.PyZipFile("testpy.zip",'w')

z0.writepy('test.py')
z0.close()

z3 = zipfile.ZipFile("testpy.zip",'r')

print("name :"+z3.filename)

print('date :')
print(z3.getinfo('test.pyc').date_time)

print(z3.getinfo('test.pyc').compress_type)
print(z3.comment)