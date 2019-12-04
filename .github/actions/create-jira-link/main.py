import os
import json
from github import Github

def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

event = read_json(os.getenv('GITHUB_EVENT_PATH'))
print(event['after'])

repo = g.get_repo(event['repository']['full_name'])
pulls = repo.get_pulls(state='open', sort='created', base='develop')
for pr in pulls:
    print(pr.number)

# or using an access token
g = Github(os.getenv('GITHUB_TOKEN'))

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)