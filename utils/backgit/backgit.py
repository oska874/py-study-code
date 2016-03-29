
from github import Github

g = Github("oska874", "GitHub1123581")


users = g.get_user()
print("I am %s",users.name)
for repo in g.get_user().get_repos():
    print(repo.name)
    print(repo.clone_url)
    print(repo.archive_url)
