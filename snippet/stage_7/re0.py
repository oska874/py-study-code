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
print("1,2 : "), 
print(m.group(1,2))

m = re.match(r"(\d+)\.?","24")
print("s: "),
print(m.groups())
print("s '0': "),
print(m.groups('1'))  #different with python shell

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict())
