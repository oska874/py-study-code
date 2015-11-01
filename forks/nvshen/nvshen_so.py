# -*- coding:utf-8 -*-
import urllib2
import sys,os
import threading
from urllib2 import HTTPError

# download adult text form caoliu
# three step:
#   1. get local file path and remote path
#   2. download file
#   3. save to local

if os.name == 'posix':
    basePath ="/tmp/nv"
else:
    basePath =r"d:\tmp\nv"

#baseUrl = "http://www.nvshen.so/wp-content/uploads/2015/"
baseUrl = "http://cl.exocl.net/htm_data/20/"

threads = []

if(os.path.exists(basePath) == False):
    if os.name == 'posix':
        os.mkdir(r"d:\tmp")
    os.mkdir(basePath)
        
def getLocalPath(mon):
    childPath = basePath + "\\" + mon
    return childPath

def getUrlPath(mon):
    childUrl = baseUrl + mon
    return childUrl

def downloadResToLocal(url1,localPath):
    try:
        request = urllib2.Request(url1)
        request.add_header("User-Agent","fake-client")
        response = urllib2.urlopen(request)
        f = file(localPath,"wb")
        f.write(response.read())
        f.close()
    except HTTPError:
        pass

def download(tmpPath,tmpUrl,sufix):
    localPath = tmpPath + sufix
    if(os.path.exists(localPath)):
        return 
    urlP = tmpUrl + sufix
    downloadResToLocal(urlP,localPath)

if __name__ == "__main__":
    startFp = 1695000
    endFp   = 1760000
    i       = 0
    maxthr  = 20
    sufix   = ".html"
    
    for sp in ("1510/","1511/","1509/"):
        for fp in (range(startFp,endFp)):
            tmpUrl = getUrlPath(str(sp)+str(fp))
            sp = sp.replace("/","_")
            tmpPath = getLocalPath(str(sp)+str(fp))
            sp = sp.replace("_","/")
            thr = threading.Thread(target=download,args=(tmpPath,tmpUrl,sufix))
            threads.append(thr)

            if (fp-startFp) % maxthr == 0:
                i+=1
                for t in threads:
                    t.start()
                for t in threads:
                    t.join()
                threads = []
                print("call :"+str(maxthr*i))
