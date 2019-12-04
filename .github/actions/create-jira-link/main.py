import os
import json
from github import Github

def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

event = read_json(os.getenv('GITHUB_EVENT_PATH'))
print(event['push'])

# or using an access token
g = Github(os.getenv('GITHUB_TOKEN'))

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)