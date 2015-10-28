import time

reps = 10000
repl = range(reps)

def timer(func,*pa,**kpa):
	start =time.clock()
	for i in repl:
		ret = func(*pa,**kpa)
	elapsed = time.clock()-start
	return (elapsed,ret) 

#print(timer(range,1,100))