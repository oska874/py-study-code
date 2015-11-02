# -*- coding:utf-8 -*-
import os,sys


#ck_dir <git repo> <dir> <local>

if __name__ == '__main__':
	args=sys.argv
	if len(args) == 4:
		git_repo_str = args[1]
		git_dir_str = args[2]
		local_dir_str = args[3]
		print(git_repo_str,git_dir_str,local_dir_str)

		os.system("git init %s" % local_dir_str)
		os.chdir(local_dir_str)
		os.system("git remote add origin %s" % git_repo_str)
		os.system("git config core.sparsecheckout true")
		#os.system("echo \"%s/\*\" >> .git/info/sparse-checkout" %local_dir_str)
		
		os.system("git pull --depth=1 origin master")

