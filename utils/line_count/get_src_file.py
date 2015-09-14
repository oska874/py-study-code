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

    if os.path.isdir(sys.argv[3]) == True:
            print("dir : "+str(True))

    fnames = os.walk(cur_dir)

    matchStr = '^(\S)*\.'+ stype + '$'
    stRe = re.compile(matchStr)

    total_line = 0

    for fn in fnames:
            for x in fn[2]:
                if sys.platform == "linux2":
			if cur_dir[-1] != '/':
				res = stRe.match(cur_dir + "/" + x)
			else:
				res = stRe.match(cur_dir + x)
				
                if res:
                    print(res.group())
                    total_line += count_lines.count_line1(res.group(),stype)

    print("total line : " + str(total_line))

