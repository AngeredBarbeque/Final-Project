#Alex Anderson, Pulling and saving info

import csv 
import json

def personal_save(users):
    with open("Project/personal.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password", "unlocked levels", "top score for each level", "preferences"])
        for user in users:
            list_thing = []
            for i in user['scores']:
                list_thing.append(i[0])
                list_thing.append(i[1])
            writer.writerow([user['name'], user['password'], user['unlocked'],*list_thing,user['preferences']])

def overall_save(level_scores):
    with open("Project/overall.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["score one", "score two", "score three", "score four", "score five", "score six", "score seven", "score eight", "score nine", "score ten"])
        for level in level_scores:
            list_thing = []
            for key, values in level.items():
                list_thing.append(values[0])
                list_thing.append(values[1])
                list_thing.append(values[2])
            writer.writerow(list_thing[:1000])

def personal_pull():
    with open("Project/personal.csv", "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)
        users = []
        for row in reader:
            user = {'name': row[0], 'password': row[1], 'unlocked': int(row[2]), 'scores': [[int(row[3]),int(row[4])],[int(row[5]),int(row[6])],[int(row[7]),int(row[8])],[int(row[9]),int(row[10])],[int(row[11]),int(row[12])],[int(row[13]),int(row[14])],[int(row[15]),int(row[16])],[int(row[17]),int(row[18])],[int(row[19]),int(row[20])],[int(row[21]),int(row[22])],[int(row[23]),int(row[24])],[int(row[25]),int(row[26])],[int(row[27]),int(row[28])],[int(row[29]),int(row[30])],[int(row[31]),int(row[32])]],'preferences':int(row[33])}
            users.append(user)
        return users

def overall_pull():
    with open("Project/overall.csv", "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        level_scores = []
        for row in reader:
            score = {
                '1':[int(row[0]), int(row[1]), row[2]],
                '2':[int(row[3]), int(row[4]), row[5]],
                '3':[int(row[6]), int(row[7]), row[8]],
                '4':[int(row[9]), int(row[10]), row[11]],
                '5':[int(row[12]), int(row[13]), row[14]],
                '6':[int(row[15]), int(row[16]), row[17]],
                '7':[int(row[18]), int(row[19]), row[20]],
                '8':[int(row[21]), int(row[22]), row[23]],
                '9':[int(row[24]), int(row[25]), row[26]],
                '10':[int(row[27]), int(row[28]), row[29]],
            }
            level_scores.append(score)
    return level_scores
