import os
import json
from github import Github


def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def parse_branch(url):
    return url.split('/')[-1]


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