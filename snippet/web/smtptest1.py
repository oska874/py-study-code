# -*- coding: utf-8 -*-
import sys
import smtplib  
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sendto = ''
mail_user = ''
mail_pass = ''
mail_postfix = ''
content = ''
mail_host = ''
mailto_list = ''
  
def send_mail(to_list, sub, content):  #to_list：收件人；sub：主题；content：邮件内容
    me = mail_user + "<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    # send text 
    #msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
    # or send multipart
    msg = MIMEMultipart()
    msg['Subject'] = sub    #subject
    msg['From'] = me
    msg['To'] = ";".join([to_list])

    att1 = MIMEText(open('./README.md', 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="read.txt"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)

    try:  
        s = smtplib.SMTP()
        s.connect(mail_host)  #connect smtp server
        s.login(mail_user, mail_pass)#login in
        print(me,to_list)
        s.sendmail(me, to_list, msg.as_string())  #send
        s.close()
        return True  
    except Exception, e:  
        print(str(e))
        return False  

if __name__ == '__main__':  
    #get names
    if len(sys.argv) < 5 :
        print("usage:\npython smtptest1.py <sendto> <sendfrom> <password> <content>")
        exit()
    else:
        sendto = sys.argv[1]
        mail_user = sys.argv[2].split('@')[0]
        mail_pass = sys.argv[3]
        mail_postfix = sys.argv[2].split('@')[1]
        content = sys.argv[4]

    print("sendto %s sendfrom %s content %s" % (sendto,mail_user,content))

# smtp server
    mailto_list = sendto
    mail_host = "smtp.126.com"  #smtp server

    if send_mail(mailto_list, content ,content):
        print("send success")
    else:
        print("send fail")