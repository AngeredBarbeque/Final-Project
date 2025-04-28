#Alex Anderson, Pulling and saving info

import csv

def personal_save(users):
    with open("Project/personal.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password", "unlocked levels", "top score for each level", "preferences"])
        for user in users:
            writer.writerow([user['name'], user['password'], user['unlocked'], user['scores'], user['preferences']])

def overall_save(level_scores):
    with open("Project/overall.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["score one", "score two", "score three", "score four", "score five", "score six", "score seven", "score eight", "score nine", "score ten"])
        for level in level_scores:
            writer.writerow([level['1'], level['2'], level['3'], level['4'], level['5'], level['6'], level['7'], level['8'], level['9'], level['10']])

def personal_pull():
    with open("Project/personal.csv", "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)
        users = []
        for row in reader:
            user = {'name': row[0], 'password': row[1], 'unlocked': row[2], 'scores': row[3], 'preferences': row[4]}
            users.append(user)
        return users

def overall_pull():
    with open("Project/overall.csv", "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)
        level_scores = []
        for row in reader:
            score = {'1': row[0], '2': row[1], '3': row[2], '4': row[3], '5': row[4], '6': row[5], '7': row[6], '8': row[7], '9': row[8], '10': row[9]}
            level_scores.append(score)
        return level_scores