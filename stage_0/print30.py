import sys

def print30(*args,**kargs):
	sep=kargs.get('sep',' ')
	end=kargs.get('end','\n')
	file=kargs.get('file',sys.stdout)
	output=''
	first=True
	for arg in args:
		output+=('' if first else sep) + str(arg)
		first=False
	file.write(output + end)



#print30("dsad","9595",end='123',sep='OO')
