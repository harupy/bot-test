import os
import json
import re
from github import Github


def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def get_actions_input(name):
    return os.getenv('INPUT_{}'.format(name).upper())


def parse_branch(url):
    pattern = r'https://api.github.com/repos/[^/]+/([^/]+)'
    m = re.match(pattern, url)
    return m.group(1) if m else ''


def parse_issue_id(branch):
    return branch.split('-')[0]


def has_duplicate(new_comment, comments):
    return new_comment in comments


def create_jira_link(issue_id):
    return 'Branch: {}'.format(issue_id)


def main():
    print(gh = Github(os.getenv('GITHUB_HEAD_REF')))
    base_url = get_actions_input('base_url')
    gh = Github(os.getenv('GITHUB_TOKEN'))
    event = read_json(os.getenv('GITHUB_EVENT_PATH'))
    branch = parse_branch(event['pull_request']['url'])
    repo = gh.get_repo(event['repository']['full_name'])

    prs = repo.get_pulls(state='open', sort='created', base='master', head=event['after'])
    pr = prs[0]

    old_comments = [c.body for c in pr.get_issue_comments()]
    new_comment = create_jira_link(branch)

    if has_duplicate(new_comment, old_comments):
        print('This pulle request already has the JIRA issue link. ')

    pr.create_issue_comment(new_comment)


if __name__ == '__main__':
    main()