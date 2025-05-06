from InquirerPy import inquirer
from info import personal_pull
from settings import *

users = personal_pull()
user = None
def main(user, users):
    while True:
        action = inquirer.select(
            message="Select an action:",
            choices=[
                "Play",
                "User Management",
                "Exit",
            ],
            default=None,
        ).execute()
        if action == "Play":
            pass
        elif action == "User Management":
            user = user_management(user, users)
        elif action == "Exit":
            break

main(user, users)