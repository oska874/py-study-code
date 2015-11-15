import pycurl
import StringIO
import urllib
 
url = "http://www.baidu.com/"
post_data_dic = {"name":"value"}
crl = pycurl.Curl()
crl.setopt(pycurl.VERBOSE,1)
crl.setopt(pycurl.FOLLOWLOCATION, 1)
crl.setopt(pycurl.MAXREDIRS, 5)
#crl.setopt(pycurl.AUTOREFERER,1)
 
crl.setopt(pycurl.CONNECTTIMEOUT, 60)
crl.setopt(pycurl.TIMEOUT, 300)
#crl.setopt(pycurl.PROXY,proxy)
crl.setopt(pycurl.HTTPPROXYTUNNEL,1)
#crl.setopt(pycurl.NOSIGNAL, 1)
crl.fp = StringIO.StringIO()
crl.setopt(pycurl.USERAGENT, "dhgu hoho")
 
# Option -d/--data <data>   HTTP POST data
crl.setopt(crl.POSTFIELDS,  urllib.urlencode(post_data_dic))
 
crl.setopt(pycurl.URL, url)
crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
crl.perform()
 
print crl.fp.getvalue()