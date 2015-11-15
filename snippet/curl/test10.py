import pycurl,select
c = pycurl.Curl()
c.setopt(pycurl.URL, "http://baidu.com")
c1 = pycurl.Curl()
c1.setopt(pycurl.URL, "http://baidu.com")
m = pycurl.CurlMulti()
m.add_handle(c)
m.add_handle(c1)
while 1:
	ret, num_handles = m.perform()
	print(ret,num_handles)
	if ret != pycurl.E_CALL_MULTI_PERFORM:
		break
print(m.fdset)
while num_handles:
    apply(select.select, m.fdset() )
    while 1:
        ret, num_handles = m.perform()
        if ret != pycurl.E_CALL_MULTI_PERFORM:
        	break