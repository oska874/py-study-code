# -*- coding: utf-8 -*-

import struct

tos0 = 'hhl'
pc = struct.pack(tos0,1,2,3)
tos1 = struct.unpack('hhl',pc)
print(tos1)
print(struct.calcsize('hhl'))

tos0 = 'ci'

pc = struct.pack(tos0,"*",123)
tos1 = struct.unpack(tos0,pc)
print(tos1)
