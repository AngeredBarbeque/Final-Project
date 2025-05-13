# Matthew Mckinley, Nicholas Larsen, Jonas Fairchild, Alex Anderson - Platform.txt

"""
TODO:
Add a 'name' category to leaderboards
Import all maps
Ensure that finishing levels & saving scores works
Playtest individual levels
"""

run = True

import os

from info import *
from user import accounts_main
from game import play_game
from leaderboards import leaderboard_printing

try:
    from InquirerPy import inquirer
    from InquirerPy.validator import EmptyInputValidator
except:
    print("You haven't installed InquirerPy yet. To do this, type 'pip install InquirerPy' into the terminal.")
    run = False

try:
    from Crypto.Cipher import AES
except:
    print("You haven't installed PyCryptoDome yet. To do this, type 'pip install PyCryptoDome' into the terminal.")
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
                    level_num = int(inquirer.number(
                        message="Select level number:",
                        min_allowed=1,
                        max_allowed=user_info["unlocked"]+1,
                        validate=EmptyInputValidator(),
                    ).execute())
                    level_num -= 1 #ALL
                    while True:
                        os.system("cls")
                        score = user_info["scores"][level_num][0]
                        coins = user_info["scores"][level_num][1]
                        if score == 100000:
                            score = "N/A"
                            coins = "N/A"
                        sub_action = inquirer.select(
                            message=f"Level {level_num+1}\nBest score: {score} seconds with {coins} coins",
                            choices=[
                                "Play",
                                "Leaderboard",
                                "Exit",
                            ],
                            default=None,
                        ).execute()

                        match sub_action:
                            case "Play":
                                user_info, level_scores = play_game(level_num, user_info, level_scores)
                                personal_save(users)
                                overall_save(level_scores)
                            case "Leaderboard":
                                leaderboard_printing(user_info, level_scores, level_num)
                                input("Done reading?: ")
                            case "Exit":
                                break

                else:
                    print("You have to log in to play the game. To do this, select 'User' on the main menu.")
                    input("Done reading?: ")
            case "User":
                user_info, users = accounts_main(users)
                personal_save(users)
            case "Tutorial":
                print("""
Login ---
If you want to save your scores, you will have to create an account. To do this, select 'User' in the main menu and then select 'Create Account'.
If you've already made an account, select 'Log in' instead.

Scores ---
Since this game is a speedrunner, every level has its own timer and leaderboard system. The top 10 overall scores will be saved, along with each player's best score for every level.
Scores are sorted based on solely time; coins are an optional collectible.

Keys ---
To move, use WASD, space, or the arrow keys while in a level.
Press Esc at any time to pause the game.

Gameplay ---              
Levers, marked with '/', open doors, marked with '|'.
Coins, an optional collectible, are marked with 'C'.
Falling blocks, marked with '▓', disappear after you stand on them.
Reach the finish (marked with 'F') to save your score.
""")
                input("Done reading?: ")
            case "Exit":
                personal_save(users)
                overall_save(level_scores)
                break

if run:
    main(users, level_scores)