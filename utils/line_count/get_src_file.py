# -*- coding: utf-8 -*- 

#usage:
#	get_src_file.py [r] dir 

import sys,os
import re
import count_lines

if __name__ == "__main__":
    argn=len(sys.argv)
    if argn < 2:
        print("usage:get_src_file.py [t]<t> <dir>")
        exit

    # get filename
    # check recurise walk dir
    # select specific type files

    if sys.argv[1] != 't':
        print("parameters error")
        exit	
    else:		
        cur_dir = sys.argv[3]
        stype = sys.argv[2]

    if os.path.isdir(sys.argv[3]) != True:
        print("path error")
        exit

    fnames = os.walk(cur_dir)
    matchStr = '^(\S)*\.'+ stype + '$'
    stRe = re.compile(matchStr)

    l1 = 0
    l2 = 0
    l3 = 0
# get file names
    for fn in fnames:
        for x in fn[2]:
            if sys.platform == "linux2":
                if os.path.isfile(cur_dir) :
                    if cur_dir[-1] != '/':
                        res = stRe.match(cur_dir + "/" + x)
                    else:
                        res = stRe.match(cur_dir + x)

                    if res:
                        aa = count_lines.count_line1(res.group(),stype)
                        l1 += aa[0]
                        l2 += aa[1]
                        l3 += aa[2]
                else:
                    print("dir " + cur_dir);

    print("source %d\ncomment %d\nempty %d" % (l1,l2,l3))
