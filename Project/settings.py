from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from login import *


def settings():
    integer_val = inquirer.number(
        message="Use Up and Down arrows to select screen size:",
        min_allowed=10,
        max_allowed=30,
        validate=EmptyInputValidator(),
    ).execute()
    return integer_val
        


def user_management(user, users):
    while True:
        if not user:
            action = inquirer.select(
                message="Select an action:",
                choices=[
                    "Log in",
                    "Exit",
                ],
                default=None,
            ).execute()
            if action == "Log in":
                user = accounts_main(users)
                continue
            elif action == "Exit":
                return user
        else:
            action = inquirer.select(
                message="Select an action:",
                choices=[
                    "Log out",
                    "Change settings",
                    "Exit",
                ],
                default=None,
            ).execute()
            if action == "Log out":
                pass
            elif action == "Change settings":
                user['preferences'] = settings()
            elif action == "Exit":
                return user