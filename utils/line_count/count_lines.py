# -*- coding: utf-8 -*- 


#usage: 
#	count_lines.py filename

import sys,os

def count_line1(fna,stype):
    fd1 = open(fna,'r')
    ret = divide_lines(fd1,stype)
    fd1.close()
    return ret 


def divide_lines(fd,ft):
    l1 = 0 # source
    l2 = 0 # comment
    l3 = 0 # empty

    if ft == 'c' or ft == 'cpp':
        multi_comment = 0
#    print("this is c/c++ files")
        for line in fd:
            if len(line) > 1:
                if multi_comment == 0:
                    # comment line start from "/*" or single line comment "//"
                    if line[0] == '/' and line[1] == '*':
                        l2 += 1
                        multi_comment = 0
                    elif line[0] == '/' and line[1] == '/':
                        l2 += 1
                    else :
                        # source line
                        l1 += 1
                elif multi_comment == 1:
                    # comment line till meet "*/"
                    l2 += 1
                    if line[-2] == '*' and line[-1] == '/':
                        multi_comment = 0
            else :
                # empty line
                l3 += 1
#        print("source %d, comment %d, empty %d" % (l1,l2,l3))
    elif ft == 'py':
        print("this is python files")
    else:
        print("not supported files "+ft)
    return (l1,l2,l3)

if __name__ == "__main__":
    argn = len(sys.argv)
    if argn < 2:
        print("usage:python count_lines.py <filename>")
        exit

    #get filename
    filename = sys.argv[1]
    print("source file: "+filename)

    ln = 0
    fd = open(filename,'r')
    for line in fd:
        if len(line) > 1:
            ln+=1
            fd.close()
#           print(filename+"has %d lines" % ln);
            if len(l2) > 1:
                if l2[0] == '/' and l2[1] == '/':
                        l1 += 0
                elif l2[0] == '/' and l2[1] == '*':
                        l1 += 0
                else:
                        l1 += 1
