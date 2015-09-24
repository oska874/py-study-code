import os

for i in range(1,254):
	print("ping :"+str(i))
	os.system("ping -n 1 192.168.0."+str(i))
	print("end")
