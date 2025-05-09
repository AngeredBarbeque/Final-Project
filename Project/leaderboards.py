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

    combined_scores.sort(key=lambda x: x[0], reverse=True)

    top_ten = combined_scores[:10]

    for i, entry in enumerate(top_ten, start=1):
        level_scores[level_number][str(i)] = entry

    return level_scores

def leaderboard_printing(user_info, level_scores, level):
    number = 0
    print(f"level {(level+1)}:")
    print(f"|placement|time|coin amount|")
    print("-" * 28)
    for i in range(9):
        number += 1
        print(f"|    {number}    |{level_scores[level][str(number)][0]}|{level_scores[level][str(number)][1]}|")
    number += 1    
    print(f"|   {number}    |{level_scores[level][str(number)][0]}|{level_scores[level][str(number)][1]}|")
    print("-" * 28)
    print(f"|   You   |{user_info['scores'][level][0]}|{user_info['scores'][level][1]}|")