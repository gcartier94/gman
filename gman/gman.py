import sys
import os
from github import Github
from config import local_config

if __name__ == '__main__':
    github_config = local_config.github_config
    access_token = github_config['access_token']
    github_url = github_config['base_url']
    org_name = github_config['org']
    g = Github(base_url=github_url, login_or_token=access_token)
    org_object = g.get_organization(org_name)
    repo_list = org_object.get_repos()
    for repo in repo_list:
        print(repo.name)
