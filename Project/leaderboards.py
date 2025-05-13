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
    
    # Loop through the first 9 placements
    for i in range(9):
        number += 1
        if str(number) in level_scores[level]:
            entry = level_scores[level][str(number)]
            if isinstance(entry, list) and len(entry) >= 4:
                if entry[0] == 100000:
                    print(f"|    {number}    |None|None|")
                else:
                    print(f"|    {number}    |{entry[3]}|{entry[0]}|{entry[1]}|{entry[2]}")
            else:
                print(f"|    {number}    |Invalid data|")
        else:
            print(f"|    {number}    |None|None|")
    
    # Handle the 10th placement
    number += 1
    if str(number) in level_scores[level]:
        entry = level_scores[level][str(number)]
        if isinstance(entry, list) and len(entry) >= 4:
            if entry[0] == 100000:
                print(f"|   {number}    |None|None|")
            else:
                print(f"|   {number}    |{entry[3]}|{entry[0]}|{entry[1]}|{entry[2]}")
        else:
            print(f"|   {number}    |Invalid data|")
    else:
        print(f"|   {number}    |None|None|")
    
    print("-" * 28)
    
    # Print the user's score
    user_score = user_info['scores'].get(level, [100000, None])
    if user_score[0] == 100000:
         print(f"|   You   |None|None|")
    else:
        print(f"|   You   |{user_score[0]}|{user_score[1]}|")
