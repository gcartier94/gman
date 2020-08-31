from PyInquirer import style_from_dict, Token, prompt, Separator
import pyfiglet


class Cli:

    def __init__(self, program_name):
        self.program_name = program_name
        self.main_style = style_from_dict({
                Token.Separator: '#6C6C6C',
                Token.QuestionMark: '#1b4eb3 bold',
                Token.Selected: '#5F819D',
                Token.Pointer: '#1b4eb3 bold',
                Token.Answer: '#5F819D bold',
                Token.Question: '',
            })
        self.main_menu_choices = [
            {
                "name": "List repositories",
                "value": "list_repos"
            },
            {
                "name": "List zones",
                "value": "list_zones",
                "disabled": "unavailable"
            },
            {
                "name": "Get repository status",
                "value": "get_repo_status",
                "disabled": "unavailable"
            },
            {
                "name": "Display organization information",
                "value": "org_info",
                "disabled": "unavailable"
            }
        ]

    def display_header(self):
        custom_fig = pyfiglet.Figlet(font='slant')
        print(custom_fig.renderText(self.program_name))

    def display_menu(self):
        self.display_header()
        question = [
            {
                "type": "list",
                "name": "main_menu",
                "message": "What would you like to do",
                "choices": self.main_menu_choices
            }
        ]
        answers = prompt(question, style=self.main_style)
        return answers