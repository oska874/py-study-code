# -*- coding: utf-8 -*-
import smtplib
import base64

filename = "./README.md"
# 读取文件内容并使用 base64 编码
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64
marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""

# 定义头部信息
part1 = """From: From Person <me@fromdomain.net>
To: To Person <amrood.admin@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# 定义消息动作
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# 定义附近部分
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
	sender = '***@126.com'
	reciever = '***@126.com'
	mail_host = 'smtp.126.com'
	mail_pass = '***'
	me = sender.split('@')[0] + "<" + sender + ">"

   	smtpObj = smtplib.SMTP()
   	smtpObj.connect(mail_host)  #connect smtp server
	smtpObj.login(sender.split('@')[0], mail_pass)  #login in
	smtpObj.sendmail(sender, reciever, message)
	smtpObj.close()
	print("Successfully sent email")
except Exception,e:
	print("Error: unable to send email")
	print(str(e))