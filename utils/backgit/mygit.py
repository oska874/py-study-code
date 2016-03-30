
from github import Github
import base64,os,subprocess

g = Github(user,password)


users = g.get_user()
print("I am %s",users.name)
os.chdir("F:/github")
for repo in g.get_user().get_repos():
    print(("./" +repo.name))
    if os.path.exists("./" +repo.name) :
        print(repo.name)
        os.chdir(repo.name)
        cmd = "git fetch ; git merge origin/master"
        subprocess.call(cmd, shell=True)
    else :
        cmd = "git clone "+repo.clone_url
        subprocess.call(cmd, shell=True)
