import pycurl

c = pycurl.Curl()
c.setopt(c.URL, '127.0.0.1')

c.setopt(c.HTTPPOST, [
    ("fileupload", (
        # upload the contents of this file
        c.FORM_FILE, __file__,
    )),
])

c.perform()
c.close()