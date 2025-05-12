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
            row = []
            for i in range(1, 11):
                value = level[str(i)]
                # Ensure it's a list before writing
                if isinstance(value, tuple):
                    value = list(value)
                row.append(value)
            writer.writerow(row)
def personal_pull():
    with open("Project/personal.csv", "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)
        users = []
        for row in reader:
            user = {'name': row[0], 'password': row[1], 'unlocked': int(row[2]), 'scores': [json.loads(row[3]),json.loads(row[4]),json.loads(row[5]),json.loads(row[6]),json.loads(row[7]),json.loads(row[8]),json.loads(row[9]),json.loads(row[10]),json.loads(row[11]),json.loads(row[12]),json.loads(row[13]),json.loads(row[14]),json.loads(row[15]),json.loads(row[16]),json.loads(row[17])], 'preferences': int(row[18])}
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

#print(overall_pull())