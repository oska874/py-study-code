# -*- coding: utf-8 -*- 


#usage: 
#	count_lines.py filename

import sys,os


# argn = len(sys.argv)
# if argn < 2:
# 	print("usage:python count_lines.py <filename>")
# 	exit

# #get filename
# filename = sys.argv[1]
# print("source file: "+filename)

# ln = 0
# fd = open(filename,'r')
# for line in fd:
# 	if len(line) > 1:
# 		ln+=1

def count_line1(fna):
	l1 = 0
	fd1 = open(fna,'r')
	for l2 in fd1:
		if len(l2) > 1:
			l1 += 1
	return l1