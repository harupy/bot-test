#!/usr/local/bin/python

import os
from github import Github

# or using an access token
g = Github(os.getenv('TOKEN'))

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)