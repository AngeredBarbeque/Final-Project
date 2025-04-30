from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

def settings():
        integer_val = inquirer.number(
        message="Use Up and Down arrows to select screen size:",
        min_allowed=10,
        max_allowed=30,
        validate=EmptyInputValidator(),
    ).execute()
        


def users(user):
    if user:
        action = inquirer.select(
            message="Select an action:",
            choices=[
                "Log in",
                "Exit",
            ],
            default=None,
        ).execute()
        if action == "Log in":
            pass
        elif action == "Change settings":
            settings()
        elif action == "Exit":
            return
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
            settings()
        elif action == "Exit":
            return

settings()