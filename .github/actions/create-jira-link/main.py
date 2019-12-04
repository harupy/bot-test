import os
from github import Github


with open(os.getenv('GITHUB_EVENT_PATH'), 'r') as f:
    print(f.read())    

# or using an access token
g = Github(os.getenv('GITHUB_TOKEN'))

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)