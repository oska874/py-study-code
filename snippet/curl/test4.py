import pycurl
c = pycurl.Curl()
c.setopt(pycurl.URL, "www.sina.com")
#c.setopt(pycurl.FOLLOWLOCATION, 1)
c.perform()
print(c.getinfo(pycurl.HTTP_CODE) , c.getinfo(pycurl.EFFECTIVE_URL))