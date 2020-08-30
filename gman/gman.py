import sys
import os
from github import Github
from config import local_config

from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2








def display_all_repos_in_org():
    github_config = local_config.github_config
    access_token = github_config['access_token']
    github_url = github_config['base_url']
    org_name = github_config['org']
    g = Github(base_url=github_url, login_or_token=access_token)
    org_object = g.get_organization(org_name)
    repo_list = org_object.get_repos()
    for repo in repo_list:
        print(repo.name)


if __name__ == '__main__':
    temp_file = open('./temp_stash.txt', 'r')
    stash_records = temp_file.readlines()
    choices = [{'name': repo_name} for repo_name in stash_records]
    question = [
    {
        'type': 'checkbox',
        'qmark': '🛠',
        'message': 'Select an item',
        'name': 'repositories',
        'choices': choices
    }]

    answer = prompt(question, style=custom_style_2)
    print(answer)