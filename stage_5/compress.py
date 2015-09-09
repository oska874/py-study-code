# -*- coding: utf-8 -*- 

import gzip,zlib

#zlib

print(zlib.adler32("abcd"))
print("compress0:")
s1 = "abcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjslabcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjslabcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjslabcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjslabcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjslabcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjslabcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjslabcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjslabcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjslabcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjslabcdefakfjdfklskladffadsfdfklds;2op3jfnnfionbvja32hnfadsfiono2fnfdssfasdfdsfsdfjladjsl"
print("compress 9")

s1c = zlib.compress(s1,9)
print("comress %d compressed %d" % (len(s1),len(s1c)))
print("decompress")
print(zlib.decompress(s1c))

s1crc = zlib.crc32(s1)
print("AAA %d" % s1crc)


#compress object
com = zlib.compressobj(9)
com2 = com.copy()
print("1compressobj")

s2cc2 = com.compress(s1)
s2cc2 += com.flush()
print("len after compress %d" % (len(s2cc2)))

print("999")
if s2cc2 == s1c:
	print("compress equal compressobj")
else:
	print("1not equal")

print("decompress  ")

s2ccd = zlib.decompress(s2cc2)
print(s2ccd)

dcom = zlib.decompressobj()


s2d = dcom.decompress(s2cc2)
print(s2d)
print(dcom.unused_data)

