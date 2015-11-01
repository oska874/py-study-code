#!/usr/bin/python

import urllib2
import sys,os
from urllib2 import HTTPError

import threading

if os.name == 'posix':
    basePath ="/tmp/vnshen_so/"
else:
    basePath =r"d:\tmp"

baseUrl = "http://www.nvshen.so/wp-content/uploads/2015/"
baseUrl = "http://cl.exocl.net/htm_data/20/" #1511/1700971.html"

threads = []

if(os.path.exists(basePath) == False):
    if os.name == 'posix':
        os.mkdir(r"d:\tmp")
    os.mkdir(basePath)
        
def getLocalPath(mon):
    childPath = basePath + "\\" + mon
    #if(os.path.exists(childPath) == False):
    #    os.mkdir(childPath)
    return childPath

def getUrlPath(mon):
    childUrl = baseUrl + mon
    return childUrl

def downloadResToLocal(url1,localPath):
    try:
        #print(url1)
        request = urllib2.Request(url1)
        request.add_header("User-Agent","fake-client")
        response = urllib2.urlopen(request)
        f = file(localPath,"wb")
        f.write(response.read())
        f.close()
    except HTTPError:
        pass

def download(tmpPath,tmpUrl):
    localPath = tmpPath + ".html" #tmpPath + str(sufx) + ".html"#".jpg"
    #print(localPath)
    if(os.path.exists(localPath)):
        return 
    #print(localPath)
    urlP = tmpUrl + ".html" # ".jpg"
    downloadResToLocal(urlP,localPath)

if __name__ == "__main__":
    startFp = 1695000
    endFp   = 1760000
    i = 0
    maxthr = 20
    for sp in ("1510/","1511/","1509/"):
        for fp in (range(startFp,endFp)):
            tmpUrl = getUrlPath(str(sp)+str(fp))
            sp = sp.replace("/","_")
            tmpPath = getLocalPath(str(sp)+str(fp))
            sp = sp.replace("_","/")
            #print(fp)
            thr = threading.Thread(target=download,args=(tmpPath,tmpUrl))
            threads.append(thr)

            if (fp-startFp) % maxthr == 0:
                i+=1
                for t in threads:
                    t.start()
                for t in threads:
                    t.join()
                threads = []
                print("call :"+str(maxthr*i))
        
