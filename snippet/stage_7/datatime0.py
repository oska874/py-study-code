# -*- coding: utf-8 -*-

import datetime


print(datetime.MINYEAR)
print(datetime.MAXYEAR)


d = datetime.date.fromordinal(730920)
print(d)
t = d.timetuple()
print(t)

ic = d.isoformat()
print(ic)

strt = d.strftime("%d/%m/%y")
print(strt)
strt = d.strftime("%A %d.%B %Y")
print(strt)
print ("the {1} is {0:%d},the {2} is {0:%B}.".format(d,"day","month"))

week = datetime.date.weekday(d)
print(week)
