import pycurl


def test(debug_type, debug_msg):
    print "debug(%d): %s" % (debug_type, debug_msg)

c = pycurl.Curl()
c.setopt(pycurl.URL, "http://curl.haxx.se/")
c.setopt(pycurl.VERBOSE, 1)
c.setopt(pycurl.DEBUGFUNCTION, test)
c.perform()