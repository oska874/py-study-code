## 1. nvshen.py
copy from web.
used for downloading picture from website with urllib2 and threading.
explain:
  - This program mainly use 2 lib : urllib2 and threading.
  - threading is used for create multi thread,like this:
  	```
    thr = threading.Thread(target=download,args=(tmpPath,tmpUrl))
  	```
  	this statement will create a thread using function "download"
  - urllib2 is used to resolve http head and address
  - and used serval libs for supporting :
    - os,sys: used for system version,path,dirs,etc
    - file: create and read/write file


