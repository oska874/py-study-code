# -*- coding: utf-8 -*-
import StringIO,cStringIO

out = StringIO.StringIO()
out.write('1234')

print>>out,"sss"

cont = out.getvalue()
print("stringio: "+cont)

out.close()

#cstringio
out = cStringIO.StringIO()
out.write('finish\n')
print>>out,'sec'

cont = out.getvalue()
print("cstringio: "+cont)
out.close()
