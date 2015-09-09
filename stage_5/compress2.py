# -*- coding: utf-8 -*- 

#gzip
import gzip

comp = open("rrr","r")



content = "Lots of content here"
with gzip.open('file.txt.gz', 'wb') as f:
	for x in comp:
	    f.write(x)
	    print(x)
	    print("*******")

print("decompress file")
with gzip.open('file.txt.gz', 'r') as f:
    file_content = f.read()
    print(file_content)
    print("-----")
comp.close()

print("%%%%%%%%%%%%1111%%%%%%%%%%%%")

comp = open('rrr','r')

fgz = gzip.GzipFile('rrr1.gz', 'wb') 
for x in comp:
	fgz.write(x)
comp.close()
fgz.close()
print("999")
fgz = gzip.open("rrr1.gz","r") 
for x in fgz:
	print(x)
	print("-------")
print("10110")




