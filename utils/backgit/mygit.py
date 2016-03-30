
from github import Github
import base64,os,sys,subprocess,shutil,urllib


def git_clone(repo,trunc):
    if trunc == True:
        shutil.rmtree("./"+repo.name,True)
    cmd = "git clone " + repo.clone_url
    subprocess.call(cmd,shell=True)

def git_pull(repo):
    chdir = os.chdir(repo.name)
    cmd = "git fetch ; git merge origin/master"
    subprocess.call(cmd,shell=True)

def git_down(repo):
    down_url = "https://github.com/XXX/XXX/archive/master.zip".replace("XXX",repo.name)
    urllib.urlretrieve(down_url,repo.name+".zip")
    print(down_url)

if __name__ == "__main__":


    if len(sys.argv) != 2:
        print("usage: python mygit.py down|pull")
        exit()
    elif sys.argv[1] != "1" and sys.argv[1] != "2":
        print("option only : 1-pull,2-download zip")
        exit()

    g = Github(user,password)

    users = g.get_user()
    print("I am %s",users.name)
    os.chdir(".")
    for repo in g.get_user().get_repos():
        if sys.argv[1] == "1": #pull
            if os.path.exists("./"+repo.name): #assume dir exist means git repo exist,to be improved
                git_pull(repo)
            else:
                git_clone(repo,False)
        elif sys.argv[1] == "2":
            git_down(repo)
        else:
            print("err %s",repo.name)
