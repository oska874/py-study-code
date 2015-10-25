#main.py

import testGblvar1

print testGblvar1.a
print testGblvar1.b
testGblvar1.modify(5,6)

print testGblvar1.a
print testGblvar1.b
testGblvar1.show()

testGblvar1.a = 1111
testGblvar1.b = 222

print testGblvar1.a
print testGblvar1.b
testGblvar1.show()

testGblvar1.a = 4444
testGblvar1.b = 3333

print testGblvar1.a
print testGblvar1.b
testGblvar1.show()