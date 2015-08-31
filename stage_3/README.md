Python call C code in two methods:

1. compile C code as dynamic link lib (.so),then using cdll call function in .so
	```
	gcc -shared mul.o libmul.so
	gcc -shared mul.o -o libmul.so
	python>>from ctypes import libmul 
	>>somelibc = windll.LoadLibrary(some.dll) 
	>>somelibc.multiply(2,3)
	6
	```

2. embedding python structure in C code
	```
	python setup.py build
	#copy add.so into current directory
	python>>import add
	>>add.add(2,3)
	5
	```

C call Python :
1. compile ccp.c
	gcc -I/usr/include/python2.7 c_call_python.c -lpython2.7