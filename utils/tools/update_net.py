# -*- coding:utf-8 -*-

#北京联通沃宽无限制提速开源实现完善版

import urllib2
import urllib
import datetime
import time
import re
import os
ContentID = urllib2.urlopen('http://bj.wokuan.cn/web/startenrequest.php').read()
ID = "".join(re.findall(r"cn=(\d*)",ContentID))
Content = urllib2.urlopen('http://bj.wokuan.cn/phoneservice/get_server_time.php').read()
YR = int("".join(re.findall(r"\"(\d*)-",Content)))
MTH = int("".join(re.findall(r"-(\d*)-",Content)))
D= int("".join(re.findall(r"-(\d*) ",Content)))
HR = int("".join(re.findall(r" (\d*):",Content)))
MIN = int("".join(re.findall(r":(\d*):",Content)))
SEC = int("".join(re.findall(r":(\d*)\"",Content)))
s = datetime.datetime(YR,MTH,D,HR,MIN,SEC)
TM = str(int(time.mktime(s.timetuple()))*1000)
data = {}
data['device'] = 'Android Phone'
data['devicename'] = 'Android Phone'
data['reqtime'] = TM
data['paras'] = '{"device":"Android Phone","devicename":"Android Phone","reqtime":"'+TM+'","upspeedcode":"09","oldspeedcode":"01","adslaccount":"'+ID+'","accetime":"300000.0","sv":"is"}'
data['accetime'] = '300000.0'
post_data = urllib.urlencode(data)
url = 'http://bj.wokuan.cn/phoneservice/mobile_improvespeed.php'
req = urllib2.urlopen(url, post_data)
res = req.read()
print("".join(re.findall(r":\"(.*)\",\"",res)))
print("Press Enter to exit.")
raw_input()