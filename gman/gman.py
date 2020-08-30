import sys
import os
from github import Github
from config import local_config

from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2

# BASIC FUNCTIONALITIES TO IMPLEMENT
# TODO - Gman lass
# TODO - Basic gman menu
# TODO - PyInquirer through all repos
# TODO - Separate repo by zones
# TODO - Display information of selected repo (branches, pr, issues)
# TODO - Stash management
# TODO - Implement rudimentary cashing technique (check last time stash has been updated?)
# TODO - Package solution


class Gman:

    def __init__(self, config_file, use_stash=False,
                 stash_path=None):
        self.stash_path = stash_path
        self.__github_config = config_file.github_config
        self.__access_token = self.__github_config['access_token']
        self.__github_url = self.__github_config['base_url']
        self.__org_name = self.__github_config['org']
        if use_stash:
            self.read_from_stash()
        else:
            self.connect_to_github()
            self.org_object = self.gh_connection.get_organization(self.__org_name)
            self.repo_list = self.org_object.get_repos()

    def connect_to_github(self):
        self.gh_connection = Github(base_url=self.__github_url,
                                    login_or_token=self.__access_token)

    def read_from_stash(self):
        if not self.stash_path:
            print('Missing stash path')
            exit(1)
        stash_file = open(self.stash_path, 'r')
        self.stash_records = stash_file.readlines()
        self.repo_list = self.stash_records

    def display_repo_list(self):
        for repo in self.repo_list:
            print(repo)


def display_menu():
    question = [
        {
            "type": "list",
            "name": "main_menu",
            "message": "What would you like to do",
            "choices": [
                {
                    "name":"List repos",
                    "value": "list"
                },
                "Update repos",
                "List Organization"
            ]
        }
    ]
    answers = prompt(question, style=custom_style_2)
    print(answers)


if __name__ == '__main__':
    '''
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
    '''
    gman = Gman(local_config, use_stash=True, stash_path='./temp_stash.txt')
    #gman.display_repo_list()
    display_menu()
