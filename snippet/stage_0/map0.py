ct=[1,2,3,4]

dt=[]

for x in ct:
	dt.append(x)

print(dt)

#----------
def ddt(sr):
	return sr+1

dt=list(map(ddt,ct))
print(dt)

dt=list(map(lambda y:y*2,ct))
print(dt)

def myreduce(func,seqs):
	ta=seqs[0]
	for ne in seqs[1:]:
		ta=func(ta,ne)
	return ta

print(myreduce((lambda x,y:x+y),[1,2,3,4,5,6]))