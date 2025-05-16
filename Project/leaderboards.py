#Alex Anderson, Updating leaderboards

from info import *

def personal_lead(user_info, level_number, new_score):
    old_score = user_info['scores'][level_number]
    if old_score[0] <= new_score[0]:
        best_score = old_score
    else:
        best_score = new_score
    user_info['scores'][level_number] = best_score
    return user_info

def overall_lead(level_scores, level_number, new_score):
    combined_scores = [[level_scores[level_number][key][0], level_scores[level_number][key][1], level_scores[level_number][key][2]] for key in level_scores[level_number]]
    combined_scores.append(new_score)

    combined_scores.sort(key=lambda x: x[0], reverse=False)

    top_ten = combined_scores[:10]

    for i, entry in enumerate(top_ten, start=1):
        level_scores[level_number][str(i)] = entry

    return level_scores

def leaderboard_printing(user_info, level_scores, level):
    print(f"| placement | name | time | coins |")
    print("-" * 33)
    # Loop through the first 9 placements
    for i in range(10):
        number = i + 1
        if level_scores[level][str(number)][0] == 100000:
            print(f"| {number} | None | None | None |")
        else:
            print(f"| {number} | {level_scores[level][str(number)][2]} | {level_scores[level][str(number)][0]} | {level_scores[level][str(number)][1]} |")
    
    print("-" * 33)
    
    # Print the user's score
    user_score = user_info['scores'][4]
    if user_score[0] == 100000:
         print(f"| - | You | None | None |")
    else:
        print(f"| - | You | {user_info['scores'][level][0]} | {user_info['scores'][level][1]} |")