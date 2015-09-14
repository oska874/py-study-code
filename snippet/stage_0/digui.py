def fn(num):
	if num == 0:
		print(num)
		return 0
	elif num == 1 :
		print(num)
		return 1
	elif num ==2 :
		print(1)
		return 1
	else:
		tp = fn(num-1) + fn(num-2)
		print(tp)
		return tp

print("fff "+str(fn(9)))

def fn1(num):
	return 0 if not num else 1 if num == 1 or num ==2 else fn1(num-1) + fn1(num-2) 

print(fn1(9))