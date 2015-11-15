import pycurl
import StringIO
 
url = "http://baidu.com/"
crl = pycurl.Curl()
crl.setopt(pycurl.VERBOSE,1)
crl.setopt(pycurl.FOLLOWLOCATION, 1)
crl.setopt(pycurl.MAXREDIRS, 5)
crl.fp = StringIO.StringIO()
crl.setopt(pycurl.URL, url)
crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
 
# Option -b/--cookie <name=string/file> Cookie string or file to read cookies from
# Note: must be a string, not a file object.
crl.setopt(pycurl.COOKIEFILE, "cookie_file_name")
 
# Option -c/--cookie-jar <file> Write cookies to this file after operation
# Note: must be a string, not a file object.
crl.setopt(pycurl.COOKIEJAR, "cookie_file_name")
 
crl.perform()
print crl.fp.getvalue()