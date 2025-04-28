#Alex Anderson, Updating leaderboards

def personal_lead(user_info, level_number, new_score):
    old_score = user_info['scores'][level_number]
    if old_score >= new_score:
        best_score = old_score
    else:
        best_score = new_score
    user_info['scores'][level_number] = best_score
    return user_info

def overall_lead(level_scores, level_number, new_score):
    combined_scores = [level_scores[level_number][key][0] for key in level_scores[level_number]]
    combined_scores.append(new_score)
    combined_scores.sort(reverse=True)
    top_ten = combined_scores[:10]
    for i, entry in enumerate(top_ten, start=1):
        level_scores[level_number][str(i)] = entry
    return level_scores