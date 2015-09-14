# doc str 
# use with class_test_3r

"file doc"
def func1(args):
	"im doc"
	'you\'re ddd no used'
	pass

class spam:
	"im spam"
	def met(self):
		"spam met"
		pass

print(func1.__doc__)
print(spam.__doc__)
print(spam.met.__doc__)
