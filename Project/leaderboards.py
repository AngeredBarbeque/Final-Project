#Alex Anderson, Updating leaderboards

from info import *

def personal_lead(user_info, level_number, new_score):
    old_score = user_info['scores'][level_number]
    if old_score[0] >= new_score[0]:
        best_score = old_score
    else:
        best_score = new_score
    user_info['scores'][level_number] = best_score
    return user_info

def overall_lead(level_scores, level_number, new_score):
    combined_scores = [(level_scores[level_number][key][0], level_scores[level_number][key][1]) for key in level_scores[level_number]]
    combined_scores.append(new_score)

    combined_scores.sort(key=lambda x: x[0], reverse=False)

    top_ten = combined_scores[:10]

    for i, entry in enumerate(top_ten, start=1):
        level_scores[level_number][str(i)] = entry

    return level_scores

def leaderboard_printing(user_info, level_scores, level):
    number = 0
    print(f"level {(level+1)}:")
    print(f"|placement|name|time|coin amount|")
    print("-" * 33)
    for i in range(9):
        number += 1
        print(level_scores[level][str(number)])
        print(level_scores[level][str(number)][1])
        if level_scores[level][str(number)][0] == 100000:
            print(f"|    {number}    |None|None|")
        else:
            print(f"|    {number}    |{level_scores[level][str(number)][3]}|{level_scores[level][str(number)][0]}|{level_scores[level][str(number)][1]}|{level_scores[level][str(number)][2]}")
    number += 1    
    if level_scores[level][str(number)][0] == 100000:
            print(f"|   {number}    |None|None|")
    else:
            print(f"|   {number}    |{level_scores[level][str(number)][0]}|{level_scores[level][str(number)][1]}|")
    print("-" * 28)
    if user_info['scores'][level][0] == 100000:
         print(f"|   You   |None|None|")
    else:
        print(f"|   You   |{user_info['scores'][level][0]}|{user_info['scores'][level][1]}|")

user_info = personal_pull()
user_info = user_info[0]
level_scores= overall_pull()
leaderboard_printing(user_info, level_scores, 0)