# -*- coding: utf-8 -*- 

import os,sys

# used in windows
for i in range(1,254):
	print("ping :"+str(i))
	os.system("ping -n 1 192.168.0."+str(i) + "> ./aa")
	print("end")
	if i % 2 == 0:
		os.system("arp -a >./ffff")
		fd = open("./ffff",'r')
		for x in fd:
			if x.find("00-04-9f-03-ae-ef") >= 0 :
				print(x)
				fd.close()
				os.system('rm ffff; rm aa')
				exit()
		fd.close()
		os.system('rm ffff')
	os.system('rm aa')



