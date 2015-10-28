# -*- coding: utf-8 -*-

import collections

#counter
cnt = collections.Counter()
for wd in (1,2,1,3,2,1,3,2,3,4,3,3,4,5):
    cnt[wd] += 1

print(cnt)

cnt1 = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt1[word] += 1
print(cnt1)

c = collections.Counter(['eggs', 'ham'])
print(c)
c['abc'] += 1
print(c)

c = collections.Counter('ajfdkdlfjk')
print(c)
print(list(c.elements()))

#deque
deq = collections.deque()
deq.append("abc")
deq.append("123")
print(deq)
deq.appendleft("^^^")
print(deq)
print(deq.count('abc'))
deq.extend('&&&&')
print(deq)
deq.pop()
print(deq)
deq.popleft()
print(deq)
deq.remove('&')
print(deq)

print(deq.reverse()) #翻转
print(deq)

deq.rotate(1) #循环移位
print(deq)
print(deq.maxlen)

#defaultdict belongs to dict,and in module collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list) #list why? using list's method,if using set,int,same to.
for k,v in s:
    d[k] = v
print(d.items())

d = {}
for k,v in s:
    d.setdefault(k,[]).append(v)
print(d.items())

s = '12345678890'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1
print(d.items())

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(set)
for k,v in s:
    d[k].add(v)
print(d.items())

po = collections.namedtuple("hellopo",['x','y'])
a1 = po(1,2)
print(a1)
print(a1.x,a1.y)

t = [1,2]
a1 = po._make(t)
print(a1)

a1 = po(x=9,y='b')
a2 = a1._asdict()
print(a2)
print(a1)

a2 = a1._replace(x='c')
print(a2)

print(a2._fields)
print(getattr(a2,'x'))

d = {'x': 11, 'y': 22}
print(po(**d))

#ordereddict
od = collections.OrderedDict()
od.__setitem__("n","1")
od.__setitem__("b","3")
od.__setitem__("m","2")
print(od)
od=sorted(od)
print(od)
