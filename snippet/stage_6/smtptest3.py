# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib

#创建一个带附件的实例
msg = MIMEMultipart()

#构造附件1
att1 = MIMEText(open('./README.md', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="read.txt"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

#加邮件头
msg['to'] = '***@126.com'
msg['from'] = '***@126.com'
msg['subject'] = 'hello world'
#发送邮件
try:
    server = smtplib.SMTP()
    server.connect('smtp.126.com')
    server.login('***','***')#XXX为用户名，XXXXX为密码
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print('发送成功')
except Exception, e:  
    print(str(e)) 