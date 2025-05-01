#Alex Anderson, Pulling and saving info

import csv
import json

def personal_save(users):
    with open("Project/personal.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password", "unlocked levels", "top score for each level", "preferences"])
        for user in users:
            writer.writerow([user['name'], user['password'], user['unlocked'], user['scores'][0], user['scores'][1], user['scores'][2], user['scores'][3], user['scores'][4], user['scores'][5], user['scores'][6], user['scores'][7], user['scores'][8], user['scores'][9], user['scores'][10], user['scores'][11], user['scores'][12], user['scores'][13], user['scores'][14], user['preferences']])

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
            user = {'name': row[0], 'password': row[1], 'unlocked': int(row[2]), 'scores': [int(row[3]),int(row[4]),int(row[5]),int(row[6]),int(row[7]),int(row[8]),int(row[9]),int(row[10]),int(row[11]),int(row[12]),int(row[13]),int(row[14]),int(row[15]),int(row[16]),int(row[17])], 'preferences': int(row[18])}
            users.append(user)
        return users

def overall_pull():
    with open("Project/overall.csv", "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)
        level_scores = []
        for row in reader:
            score = {'1': json.loads(row[0]), '2': json.loads(row[1]), '3': json.loads(row[2]), '4': json.loads(row[3]), '5': json.loads(row[4]), '6': json.loads(row[5]), '7': json.loads(row[6]), '8': json.loads(row[7]), '9': json.loads(row[8]), '10': json.loads(row[9])}
            level_scores.append(score)
        return level_scores
