from InquirerPy import inquirer

def main():
    while True:
        action = inquirer.select(
            message="Select an action:",
            choices=[
                "Play",
                "User",
                "Exit",
            ],
            default=None,
        ).execute()
        if action == "Play":
            pass
        elif action == "User":
            pass
        elif action == "Exit":
            break