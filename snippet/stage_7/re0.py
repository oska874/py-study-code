# -*- coding: utf-8 -*-
import re


src = r'\123'
print("src: "+src)

re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
res = re_ip.match(r"101.2.32.4")
if res == None :
    print("0 not match")
else :
    print("0 match: " + res.group())
    
re_str = re.compile("^starting$")
res = re_str.match(r"starting")
if res == None :
    print("1 not match")
else :
    print("0 match: " + res.group())

print(re.IGNORECASE)
print(re.LOCALE)

res = re.match("^abc","abcdef")
if res != None:
    print("match \"^abc\" : " + res.group()) 

res = re.match("^a{1,3}?","aaa")
if res != None:
    print("match \"^a{1,3}\" : " + res.group()) 

res = re.search("ab","aaba")
res1 = re.match("ab","aaba")
if res != None:
    print("search : " + res.group())
if res1 != None:
    print("match : " +res1.group())


sp0 = re.split('\W+', 'Words, words, words.')
print("split : "),
print(sp0)

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print("all : " +m.group(0))
print("1 : " + m.group(1))
print("2 " + m.group(2))
print("1,2 : "), 
print(m.group(1,2))

m = re.match(r"(\d+)\.?","24")
print("s: "),
print(m.groups())
print("s '0': "),
print(m.groups('1'))  #different with python shell

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict())

#-----------------------------------------
fa_str = "ab cd ab de abc dab"
f = re.findall('ab',fa_str)
if f != None:
    print(f)
    print(len(f))

fa_str = "ab cd ab de abc dab"
f = re.finditer('ab',fa_str)
print(f)

#sub
sub_str = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',r'static PyObject*\npy_\1(void)\n{','def myfunc():')
if sub_str != None:
    print(sub_str)
else:
    print("no subs")

print("")
sub_str = re.subn(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',r'static PyObject*\npy_\1(void)\n{','def myfunc():')
if sub_str != None:
    print(sub_str)
else:
    print("no subs")
re.purge()

ps = re.match(r"(?P<aaa>\w+) (?P<bbb>\w+)","Malcolm Reynolds")
if ps:
    print(ps.groupdict())
    print(ps.pos)

#
def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

valid = re.compile(r"^[a2-9tjqk]{5}$")
poker = displaymatch(valid.match("akt5q"))
print(poker)
poker = displaymatch(valid.match("akt5e"))
print(poker)
poker = displaymatch(valid.match("727ak"))
print(poker)


##
text = "abc def ghi 123 456 huf j79 9fa *f2f"
print(text)

print([re.split(":? ", entry, 1) for entry in re.split('\n+',text)])
print([re.split(":? ", entry, 2) for entry in re.split('\n+',text)])
print([re.split(":? ", entry, 3) for entry in re.split('\n+',text)])

##sub func
import random
def repl(m):
    inner_word = list(m.group(2))
    print(inner_word)
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)
text = "Professor Abdolmalek, please report your absences promptly."
s1 = re.sub(r"(\w)(\w+)(\w)", repl, text)
s2 = re.sub(r"(\w)(\w+)(\w)", repl, text)
print(text)
print(s1)
print(s2)

r12 = re.search(r"(\w)","abcde")
print(r12.groups())
m = re.match(r"(\d+)\.(\d+)", "24.1632")
print(m.groups())