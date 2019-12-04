import os
import json
import re
from github import Github


def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def parse_branch(url):
    pattern = r'https://api.github.com/repos/[^/]+/([^/]+)'
    m = re.match(pattern, url)
    return m.group(1) if m else ''


def parse_issue_id(branch):
    return branch.split('-')[0]


def create_jira_link(issue_id):
    pass


def main():
    # or using an access token
    g = Github(os.getenv('GITHUB_TOKEN'))

    event = read_json(os.getenv('GITHUB_EVENT_PATH'))
    print(event)
    print(list(event['pull_request'].keys()))
    print(event['after'])

    branch = parse_branch(event['pull_request']['url'])
    print(branch)

    repo = g.get_repo(event['repository']['full_name'])
    pulls = repo.get_pulls(state='open', sort='created', base='master')
    for pr in pulls:
        for comment in pr.get_issue_comments():  # get_comments only get review comments
            print(comment.body)
            print(dir(comment))

        pr.create_issue_comment('Branch: {}'.format(branch))

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        print(repo.name)



if __name__ == '__main__':
    main()