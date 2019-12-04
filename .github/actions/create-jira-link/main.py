import os
from github import Github

print(os.getenv('GITHUB_EVENT_PATH'))

# or using an access token
g = Github(os.getenv('GITHUB_TOKEN'))

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)