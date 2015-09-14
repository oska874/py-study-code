# class definition
class First_class:
	owner=''
	data=0
	def __init__(self,val):
		self.owner = val

	def setdata(self,dat):
		self.data = dat



# class inherit
class Second_class(First_class):
	def getdatas(self):
		return [self.owner,self.data]
	def __str__ (self):
		return '%s' % self.data

'''
	def getdata():
		return self.data
'''


t2 = Second_class('ezio')
t2.setdata(123)

print(t2.getdatas())
print(str(t2.data))

t2.data2 = 'hello world'

print(t2.data2)

'''
t3 = Second_class('zhu')
print(t3.data2)
'''

# operators override
# multi inherit
class Third_class(Second_class,First_class):
	def __init__(self,owner,dat1,dat2):
		self.data2 = dat2
		self.data1 = dat1
		self.owner = owner
	def __add__(self,other):
		self.data1 += other
		self.data2 += other
		return self

t4 = Third_class('wang',1,100)
print(t4.data2)
print(t2.data2)

t4+=9
print(t4.data1,t4.data2)


class rec:pass

'''
if rec.name :
	rec.name = 'bob'
print(rec.name)
'''

r1 = rec()

r1.nn = '111'
print(r1.nn)

def met1(self,dat):
	self.data1=dat

# add method for class rec. 
# the reason why class function must list self out
rec.method1 = met1

# equal usage
r1.method1(12)
print(r1.data1)

rec.method1(r1,13)

print(r1.data1)

# father class's init should be called explicit
class Fourth_class(First_class):
	def __init__(self,owner,empe):
		First_class.__init__(self,owner)
		self.empe = empe ;

t5 = Fourth_class("liu",'wu')
print(t5.owner)


if __name__ == '__main__':
	print("1111111")
else:
	print('2222')