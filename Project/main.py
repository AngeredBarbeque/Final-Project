
run = True

import os

from info import *

try:
    from InquirerPy import inquirer
except:
    print("You haven't installed InquirerPy yet. To do this, type 'pip install InquirerPy' into the terminal.")
    run = False

users = personal_pull()
level_scores = overall_pull()

def main(users, level_scores):
    user_info = None

    while True:
        os.system('cls')
        action = inquirer.select(
            message="Platform.txt",
            choices=[
                "Play",
                "User",
                "Tutorial",
                "Exit",
            ],
            default=None,
        ).execute()

        match action:
            case "Play":
                if user_info:
                    pass
                else:
                    print("You have to log in to play the game. To do this, select 'User' on the main menu.")
                    input("Done reading?:")

            case "User":
                #user_info = ...
                pass
            case "Tutorial":
                print("""
Login ---
If you want to save your scores, you will have to create an account. To do this, select 'User' in the main menu and then select 'Create Account'.
If you've already made an account, select 'Log in' instead.

Scores ---
Since this game is a speedrunner, every level has its own timer and leaderboard system. The top 10 overall scores will be saved, along with each player's best score for every level.
Scores are sorted based on solely time; coins are an optional collectible.

Gameplay ---
To move, use WASD, space, or the arrow keys while in a level.
Levers, marked with '/', open doors, marked with '|'.
Coins, an optional collectible, are marked with 'C'.
Falling blocks, marked with '▓', disappear after you stand on them.
Reach the finish (marked with 'F') to save your time.
""")
                input("Done reading?: ")
            case "Exit":
                #Save things
                break

if run:
    main(users, level_scores)