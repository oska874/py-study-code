# -*- coding: utf-8 -*- 

import bz2

z1 = bz2.BZ2File('test.bz2','r')
str1 = z1.read()

z1.close()

z0 = bz2.BZ2File("test.bz2",'w')
z0.write(str1)
z0.write('aaaaaaaa123456789\n')
z0.writelines('99999999999999999\n')
z0.close()

z0 = bz2.BZ2File('test.bz2','r')
str1 = z0.read()
print(str1)

#how?
#有问题，压缩结果
z2 = bz2.BZ2Compressor(1)
a1 = z2.compress("123456hfajfhkdahfeinvjsmklasdlnveiornhigrngrjengker,zkadlfkeknka789123456789\n")
z2.flush()
print(a1)
z3 = bz2.BZ2Decompressor()
a2 = z3.decompress(a1)
print(a2)

a1 = bz2.compress('95f9ads5f9ds5f9ads',5)
print(a1)

