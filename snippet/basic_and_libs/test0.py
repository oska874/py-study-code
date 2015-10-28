import sys,os,platform

print(os.path)

if os.path.exists('d:\download') == False:
	print("1111")
else:
	print("2222")

if os.name == 'nt':
	print("this is windows")


print(platform.dist())
print(platform.node())
print(platform.uname())
print(platform.machine())

print("abc: "+str(platform.mac_ver()))
print("aaa: "+str(platform.win32_ver() ))