import pycurl

def body(buf):
	return len(buf)
def header(buf):
	return len(buf)
## Callback function invoked when download/upload has progress
def progress(download_t, download_d, upload_t, upload_d):
    print "Total to download", download_t
    print "Total downloaded", download_d
    print "Total to upload", upload_t
    print "Total uploaded", upload_d

c = pycurl.Curl()
c.setopt(c.URL, "http://slashdot.org/")
c.setopt(c.NOPROGRESS, 0)
c.setopt(c.PROGRESSFUNCTION, progress)
c.setopt(pycurl.WRITEFUNCTION, body)
c.setopt(pycurl.HEADERFUNCTION, header)
c.perform()