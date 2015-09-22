import smtplib

sender = 'acdsee8aa@126.com'
receivers = ['acdsee7aa@126.com']

message = """From: From Person <acdsee8aa@126.com>
To: To Person <acdsee7aa@126.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.126.com')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"