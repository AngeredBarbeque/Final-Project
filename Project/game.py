import os
import time
import copy
import threading

from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

from leaderboards import *

# Helper functions ----------------------------------------------------------------------------------------------------------------

def area(x1, y1, x2, y2): # Defines a function which takes two coordinate points and selects every point between them.
    area_list = []
    for y in range(y2, y1 - 1, -1):
        for x in range(x1, x2 + 1):
            area_list.append({'x': x, 'y': y})
    return area_list

def get_block(coord, p, map):
    block_returns = []
    if coord == {"x": p["x_pos"], "y": p["y_pos"]}:
        block_returns.append(p["name"])

    for block in map:
        if block["coord"] == coord:
            block_returns.append(block["type"])
    
    block_returns.append(" ")
    return block_returns

# Physics and Display -------------------------------------------------------------------------------------------------------------

def display(map, p): # Displays the screen around the player based on their selected screen size.
    os.system("cls")
    s = int(p["preferences"]["screen_size"]/2)
    prev_y = p["y_pos"] + s
    row = []
    for space in area(p["x_pos"] - s, p["y_pos"] - s, p["x_pos"] + s, p["y_pos"] + s):
        if space["y"] != prev_y:
            for i in row:
                print(i, end='')
            print()
            row = []
        row.append(get_block(space, p, map)[0])
        prev_y = space["y"]

def collision(map, p):
    collision_returns = []
    player_block = get_block({"x": p["x_pos"], "y": p["y_pos"]}, p, map)[1]
    if player_block in ['<', '>', 'v', '^', '*'] or p["y_pos"] < -50:
        collision_returns.append('dead')
    if player_block == 'C':
        collision_returns.append('coin')
    if player_block == 'F':
        collision_returns.append('fin')
    if player_block == '/':
        collision_returns.append('lever')

    if get_block({"x": p["x_pos"], "y": p["y_pos"]-1}, p, map)[0] in ["█", "▓", "|"]:
        collision_returns.append('down')
    if get_block({"x": p["x_pos"], "y": p["y_pos"]+1}, p, map)[0] in ["█", "▓", "|"]:
        collision_returns.append('up')
    if get_block({"x": p["x_pos"]-1, "y": p["y_pos"]}, p, map)[0] in ["█", "▓", "|"]:
        collision_returns.append('left')
    if get_block({"x": p["x_pos"]+1, "y": p["y_pos"]}, p, map)[0] in ["█", "▓", "|"]:
        collision_returns.append('right')

    if get_block({"x": p["x_pos"], "y": p["y_pos"]-1}, p, map)[0] == "▓":
        collision_returns.append('falling')

    return collision_returns

# Game Master Function ------------------------------------------------------------------------------------------------------------

def passive_move(map, p):
    colls = collision(map, p)
    if 'down' in colls:
        if p["y_vel"] < 0:
            p["y_vel"] = 0
    elif p["y_vel"] > -0.5:
        p["y_vel"] -= 0.2 #UNDECIDED                                                                                                                                                                  ---
    if 'up' in colls and p["y_vel"] > 0:
        p["y_vel"] = 0

    if 'left' in colls and p["x_vel"] < 0:
        p["x_vel"] = 0
    if 'right' in colls and p["x_vel"] > 0:
        p["x_vel"] = 0

    p["x_pos_acc"] += p["x_vel"]
    p["y_pos_acc"] += p["y_vel"]
    p["x_pos"] = round(p["x_pos_acc"])
    p["y_pos"] = round(p["y_pos_acc"])
    return p

user_info = {"name": "Jonas", "preferences": 20}


def play_game(map_num, user_info, level_scores):
    run = True
    try:
        import keyboard

        def active_move(map, p):
            colls = collision(map, p)
            pressed = []
            for i in ["w", "up", "space"]:
                if keyboard.is_pressed(i):
                    pressed.append("up")
            for i in ["a", "left"]:
                if keyboard.is_pressed(i):
                    pressed.append("left")
            for i in ["d", "right"]:
                if keyboard.is_pressed(i):
                    pressed.append("right")

            if 'up' in pressed and 'down' in colls and 'up' not in colls:
                p["y_vel"] = 1.28 #UNDECIDED                                                                                                                                                                  ---

            if 'left' in pressed:
                if p["x_vel"] > -0.5 and 'left' not in colls:
                    p["x_vel"] -= 0.2 #UNDECIDED                                                                                                                                                                  ---
            else:
                if p["x_vel"] >= -0.1 and p["x_vel"] <= 0:
                    p["x_vel"] = 0
                elif p["x_vel"] < 0.1:
                    p["x_vel"] += 0.2 #UNDECIDED                                                                                                                                                                  ---
    
            if 'right' in pressed:
                if p["x_vel"] < 0.5 and 'right' not in colls:
                    p["x_vel"] += 0.2 #UNDECIDED                                                                                                                                                                  ---
            else:
                if p["x_vel"] <= 0.1 and p["x_vel"] >= 0:
                    p["x_vel"] = 0
                elif p["x_vel"] > 0.1:
                    p["x_vel"] -= 0.2 #UNDECIDED                                                                                                                                                                  ---

            return p

    except:
        run = False
        print("You haven't installed the keyboard module yet. To do this, type 'pip install keyboard' into the terminal.")

    def falling_block(player, fallings):
        p = copy.deepcopy(player)
        if {"x": p["x_pos"], "y": p["y_pos"]-1} not in fallings:
            fallings.append({"x": p["x_pos"], "y": p["y_pos"]-1})
            pos = {"x": p["x_pos"], "y": p["y_pos"]-1}

            falling = map.index({"coord":pos,"type":"▓"})
            time.sleep(.5)
            del map[falling]
            time.sleep(2)
            map.insert(falling, {"coord":pos,"type":"▓"})

            del fallings[fallings.index(pos)]

    maps = [
        [
            {"coord":{"x":130,"y":20},"type":"█"},{"coord":{"x":131,"y":20},"type":">"},{"coord":{"x":130,"y":19},"type":"█"},{"coord":{"x":131,"y":19},"type":">"},{"coord":{"x":110,"y":18},"type":"C"},{"coord":{"x":130,"y":18},"type":"█"},{"coord":{"x":130,"y":17},"type":"█"},{"coord":{"x":91,"y":16},"type":"F"},{"coord":{"x":108,"y":16},"type":"^"},{"coord":{"x":113,"y":16},"type":"^"},{"coord":{"x":130,"y":16},"type":"|"},{"coord":{"x":88,"y":15},"type":"█"},{"coord":{"x":89,"y":15},"type":"█"},{"coord":{"x":90,"y":15},"type":"█"},{"coord":{"x":91,"y":15},"type":"█"},{"coord":{"x":92,"y":15},"type":"█"},{"coord":{"x":93,"y":15},"type":"█"},{"coord":{"x":94,"y":15},"type":"█"},{"coord":{"x":95,"y":15},"type":"▓"},{"coord":{"x":96,"y":15},"type":"▓"},{"coord":{"x":97,"y":15},"type":"▓"},{"coord":{"x":98,"y":15},"type":"▓"},{"coord":{"x":99,"y":15},"type":"▓"},{"coord":{"x":100,"y":15},"type":"▓"},{"coord":{"x":101,"y":15},"type":"▓"},{"coord":{"x":102,"y":15},"type":"▓"},{"coord":{"x":103,"y":15},"type":"▓"},{"coord":{"x":104,"y":15},"type":"▓"},{"coord":{"x":105,"y":15},"type":"▓"},{"coord":{"x":106,"y":15},"type":"▓"},{"coord":{"x":107,"y":15},"type":"▓"},{"coord":{"x":108,"y":15},"type":"▓"},{"coord":{"x":109,"y":15},"type":"▓"},{"coord":{"x":110,"y":15},"type":"▓"},{"coord":{"x":111,"y":15},"type":"▓"},{"coord":{"x":112,"y":15},"type":"▓"},{"coord":{"x":113,"y":15},"type":"▓"},{"coord":{"x":114,"y":15},"type":"▓"},{"coord":{"x":115,"y":15},"type":"▓"},{"coord":{"x":116,"y":15},"type":"▓"},{"coord":{"x":117,"y":15},"type":"▓"},{"coord":{"x":118,"y":15},"type":"▓"},{"coord":{"x":119,"y":15},"type":"▓"},{"coord":{"x":120,"y":15},"type":"▓"},{"coord":{"x":121,"y":15},"type":"▓"},{"coord":{"x":122,"y":15},"type":"▓"},{"coord":{"x":123,"y":15},"type":"▓"},{"coord":{"x":124,"y":15},"type":"▓"},{"coord":{"x":125,"y":15},"type":"▓"},{"coord":{"x":126,"y":15},"type":"▓"},{"coord":{"x":127,"y":15},"type":"█"},{"coord":{"x":128,"y":15},"type":"█"},{"coord":{"x":129,"y":15},"type":"█"},{"coord":{"x":130,"y":15},"type":"█"},{"coord":{"x":131,"y":15},"type":"█"},{"coord":{"x":132,"y":15},"type":"█"},{"coord":{"x":133,"y":15},"type":"█"},{"coord":{"x":134,"y":15},"type":"█"},{"coord":{"x":135,"y":15},"type":"█"},{"coord":{"x":136,"y":15},"type":"█"},{"coord":{"x":137,"y":15},"type":"█"},{"coord":{"x":138,"y":15},"type":"█"},{"coord":{"x":95,"y":14},"type":"*"},{"coord":{"x":96,"y":14},"type":"*"},{"coord":{"x":97,"y":14},"type":"*"},{"coord":{"x":98,"y":14},"type":"*"},{"coord":{"x":99,"y":14},"type":"*"},{"coord":{"x":100,"y":14},"type":"*"},{"coord":{"x":101,"y":14},"type":"*"},{"coord":{"x":102,"y":14},"type":"*"},{"coord":{"x":103,"y":14},"type":"*"},{"coord":{"x":104,"y":14},"type":"*"},{"coord":{"x":105,"y":14},"type":"*"},{"coord":{"x":106,"y":14},"type":"*"},{"coord":{"x":107,"y":14},"type":"*"},{"coord":{"x":108,"y":14},"type":"*"},{"coord":{"x":109,"y":14},"type":"*"},{"coord":{"x":110,"y":14},"type":"*"},{"coord":{"x":111,"y":14},"type":"*"},{"coord":{"x":112,"y":14},"type":"*"},{"coord":{"x":113,"y":14},"type":"*"},{"coord":{"x":114,"y":14},"type":"*"},{"coord":{"x":115,"y":14},"type":"*"},{"coord":{"x":116,"y":14},"type":"*"},{"coord":{"x":117,"y":14},"type":"*"},{"coord":{"x":118,"y":14},"type":"*"},{"coord":{"x":119,"y":14},"type":"*"},{"coord":{"x":120,"y":14},"type":"*"},{"coord":{"x":121,"y":14},"type":"*"},{"coord":{"x":122,"y":14},"type":"*"},{"coord":{"x":123,"y":14},"type":"*"},{"coord":{"x":124,"y":14},"type":"*"},{"coord":{"x":125,"y":14},"type":"*"},{"coord":{"x":126,"y":14},"type":"*"},{"coord":{"x":155,"y":13},"type":"/", "door":[{"x":130,"y":16}]},{"coord":{"x":144,"y":12},"type":"█"},{"coord":{"x":145,"y":12},"type":"█"},{"coord":{"x":146,"y":12},"type":"█"},{"coord":{"x":147,"y":12},"type":"█"},{"coord":{"x":153,"y":12},"type":"█"},{"coord":{"x":154,"y":12},"type":"█"},{"coord":{"x":155,"y":12},"type":"█"},{"coord":{"x":135,"y":10},"type":"█"},{"coord":{"x":136,"y":10},"type":"█"},{"coord":{"x":137,"y":10},"type":"█"},{"coord":{"x":138,"y":10},"type":"█"},{"coord":{"x":139,"y":10},"type":"█"},{"coord":{"x":140,"y":10},"type":"█"},{"coord":{"x":141,"y":10},"type":"█"},{"coord":{"x":133,"y":9},"type":"█"},{"coord":{"x":134,"y":9},"type":"█"},{"coord":{"x":135,"y":9},"type":"█"},{"coord":{"x":136,"y":9},"type":"█"},{"coord":{"x":137,"y":9},"type":"█"},{"coord":{"x":133,"y":8},"type":"█"},{"coord":{"x":134,"y":8},"type":"█"},{"coord":{"x":135,"y":8},"type":"█"},{"coord":{"x":127,"y":7},"type":"^"},{"coord":{"x":133,"y":7},"type":"█"},{"coord":{"x":134,"y":7},"type":"█"},{"coord":{"x":135,"y":7},"type":"█"},{"coord":{"x":-4,"y":6},"type":"█"},{"coord":{"x":-3,"y":6},"type":"█"},{"coord":{"x":-2,"y":6},"type":"█"},{"coord":{"x":-1,"y":6},"type":"█"},{"coord":{"x":0,"y":6},"type":"█"},{"coord":{"x":1,"y":6},"type":"█"},{"coord":{"x":2,"y":6},"type":"█"},{"coord":{"x":3,"y":6},"type":"█"},{"coord":{"x":4,"y":6},"type":"█"},{"coord":{"x":5,"y":6},"type":"█"},{"coord":{"x":6,"y":6},"type":"█"},{"coord":{"x":7,"y":6},"type":"█"},{"coord":{"x":8,"y":6},"type":"█"},{"coord":{"x":9,"y":6},"type":"█"},{"coord":{"x":10,"y":6},"type":"█"},{"coord":{"x":11,"y":6},"type":"█"},{"coord":{"x":12,"y":6},"type":"█"},{"coord":{"x":13,"y":6},"type":"█"},{"coord":{"x":14,"y":6},"type":"█"},{"coord":{"x":15,"y":6},"type":"█"},{"coord":{"x":124,"y":6},"type":"█"},{"coord":{"x":125,"y":6},"type":"█"},{"coord":{"x":126,"y":6},"type":"█"},{"coord":{"x":127,"y":6},"type":"█"},{"coord":{"x":128,"y":6},"type":"█"},{"coord":{"x":129,"y":6},"type":"█"},{"coord":{"x":130,"y":6},"type":"█"},{"coord":{"x":131,"y":6},"type":"█"},{"coord":{"x":132,"y":6},"type":"█"},{"coord":{"x":133,"y":6},"type":"█"},{"coord":{"x":134,"y":6},"type":"█"},{"coord":{"x":135,"y":6},"type":"█"},{"coord":{"x":-4,"y":5},"type":"█"},{"coord":{"x":-3,"y":5},"type":"█"},{"coord":{"x":-4,"y":4},"type":"█"},{"coord":{"x":-3,"y":4},"type":"█"},{"coord":{"x":62,"y":4},"type":"█"},{"coord":{"x":63,"y":4},"type":"█"},{"coord":{"x":64,"y":4},"type":"█"},{"coord":{"x":65,"y":4},"type":"█"},{"coord":{"x":66,"y":4},"type":"█"},{"coord":{"x":67,"y":4},"type":"█"},{"coord":{"x":68,"y":4},"type":"█"},{"coord":{"x":69,"y":4},"type":"█"},{"coord":{"x":70,"y":4},"type":"█"},{"coord":{"x":71,"y":4},"type":"█"},{"coord":{"x":72,"y":4},"type":"█"},{"coord":{"x":73,"y":4},"type":"█"},{"coord":{"x":114,"y":4},"type":"█"},{"coord":{"x":115,"y":4},"type":"█"},{"coord":{"x":116,"y":4},"type":"█"},{"coord":{"x":117,"y":4},"type":"█"},{"coord":{"x":118,"y":4},"type":"█"},{"coord":{"x":-7,"y":3},"type":"█"},{"coord":{"x":-6,"y":3},"type":"█"},{"coord":{"x":-5,"y":3},"type":"█"},{"coord":{"x":-4,"y":3},"type":"█"},{"coord":{"x":62,"y":3},"type":"v"},{"coord":{"x":63,"y":3},"type":"v"},{"coord":{"x":64,"y":3},"type":"v"},{"coord":{"x":65,"y":3},"type":"v"},{"coord":{"x":66,"y":3},"type":"v"},{"coord":{"x":67,"y":3},"type":"v"},{"coord":{"x":68,"y":3},"type":"v"},{"coord":{"x":69,"y":3},"type":"v"},{"coord":{"x":70,"y":3},"type":"v"},{"coord":{"x":71,"y":3},"type":"v"},{"coord":{"x":72,"y":3},"type":"v"},{"coord":{"x":73,"y":3},"type":"v"},{"coord":{"x":97,"y":3},"type":"█"},{"coord":{"x":98,"y":3},"type":"█"},{"coord":{"x":99,"y":3},"type":"█"},{"coord":{"x":100,"y":3},"type":"█"},{"coord":{"x":101,"y":3},"type":"█"},{"coord":{"x":-7,"y":2},"type":"█"},{"coord":{"x":-6,"y":2},"type":"█"},{"coord":{"x":33,"y":2},"type":"█"},{"coord":{"x":34,"y":2},"type":"█"},{"coord":{"x":35,"y":2},"type":"█"},{"coord":{"x":36,"y":2},"type":"█"},{"coord":{"x":92,"y":2},"type":"█"},{"coord":{"x":93,"y":2},"type":"█"},{"coord":{"x":94,"y":2},"type":"█"},{"coord":{"x":95,"y":2},"type":"█"},{"coord":{"x":96,"y":2},"type":"█"},{"coord":{"x":-7,"y":1},"type":"█"},{"coord":{"x":79,"y":1},"type":"█"},{"coord":{"x":80,"y":1},"type":"█"},{"coord":{"x":81,"y":1},"type":"█"},{"coord":{"x":82,"y":1},"type":"█"},{"coord":{"x":83,"y":1},"type":"█"},{"coord":{"x":84,"y":1},"type":"█"},{"coord":{"x":85,"y":1},"type":"█"},{"coord":{"x":105,"y":1},"type":"█"},{"coord":{"x":106,"y":1},"type":"█"},{"coord":{"x":107,"y":1},"type":"█"},{"coord":{"x":108,"y":1},"type":"█"},{"coord":{"x":109,"y":1},"type":"█"},{"coord":{"x":125,"y":1},"type":"C"},{"coord":{"x":-7,"y":0},"type":"█"},{"coord":{"x":-5,"y":0},"type":"C"},{"coord":{"x":12,"y":0},"type":"^"},{"coord":{"x":13,"y":0},"type":"^"},{"coord":{"x":14,"y":0},"type":"^"},{"coord":{"x":26,"y":0},"type":"█"},{"coord":{"x":27,"y":0},"type":"█"},{"coord":{"x":28,"y":0},"type":"█"},{"coord":{"x":29,"y":0},"type":"█"},{"coord":{"x":30,"y":0},"type":"█"},{"coord":{"x":31,"y":0},"type":"█"},{"coord":{"x":59,"y":0},"type":"█"},{"coord":{"x":60,"y":0},"type":"█"},{"coord":{"x":61,"y":0},"type":"█"},{"coord":{"x":62,"y":0},"type":"█"},{"coord":{"x":63,"y":0},"type":"█"},{"coord":{"x":64,"y":0},"type":"█"},{"coord":{"x":65,"y":0},"type":"█"},{"coord":{"x":66,"y":0},"type":"█"},{"coord":{"x":67,"y":0},"type":"█"},{"coord":{"x":68,"y":0},"type":"█"},{"coord":{"x":69,"y":0},"type":"█"},{"coord":{"x":70,"y":0},"type":"█"},{"coord":{"x":71,"y":0},"type":"█"},{"coord":{"x":72,"y":0},"type":"█"},{"coord":{"x":73,"y":0},"type":"█"},{"coord":{"x":123,"y":0},"type":"█"},{"coord":{"x":124,"y":0},"type":"█"},{"coord":{"x":125,"y":0},"type":"█"},{"coord":{"x":126,"y":0},"type":"█"},{"coord":{"x":127,"y":0},"type":"█"},{"coord":{"x":-7,"y":-1},"type":"█"},{"coord":{"x":-6,"y":-1},"type":"█"},{"coord":{"x":-5,"y":-1},"type":"█"},{"coord":{"x":-4,"y":-1},"type":"█"},{"coord":{"x":-3,"y":-1},"type":"█"},{"coord":{"x":-2,"y":-1},"type":"█"},{"coord":{"x":-1,"y":-1},"type":"█"},{"coord":{"x":0,"y":-1},"type":"█"},{"coord":{"x":1,"y":-1},"type":"█"},{"coord":{"x":2,"y":-1},"type":"█"},{"coord":{"x":3,"y":-1},"type":"█"},{"coord":{"x":4,"y":-1},"type":"█"},{"coord":{"x":5,"y":-1},"type":"█"},{"coord":{"x":6,"y":-1},"type":"█"},{"coord":{"x":7,"y":-1},"type":"█"},{"coord":{"x":8,"y":-1},"type":"█"},{"coord":{"x":9,"y":-1},"type":"█"},{"coord":{"x":10,"y":-1},"type":"█"},{"coord":{"x":11,"y":-1},"type":"█"},{"coord":{"x":12,"y":-1},"type":"█"},{"coord":{"x":13,"y":-1},"type":"█"},{"coord":{"x":14,"y":-1},"type":"█"},{"coord":{"x":15,"y":-1},"type":"█"},{"coord":{"x":16,"y":-1},"type":"█"},{"coord":{"x":19,"y":-1},"type":"█"},{"coord":{"x":20,"y":-1},"type":"█"},{"coord":{"x":21,"y":-1},"type":"█"},{"coord":{"x":22,"y":-1},"type":"█"},{"coord":{"x":23,"y":-1},"type":"█"},{"coord":{"x":40,"y":-1},"type":"█"},{"coord":{"x":41,"y":-1},"type":"█"},{"coord":{"x":42,"y":-1},"type":"█"},{"coord":{"x":46,"y":-1},"type":"▓"},{"coord":{"x":47,"y":-1},"type":"▓"},{"coord":{"x":48,"y":-1},"type":"▓"},{"coord":{"x":49,"y":-1},"type":"▓"},{"coord":{"x":50,"y":-1},"type":"▓"},{"coord":{"x":51,"y":-1},"type":"▓"},{"coord":{"x":52,"y":-1},"type":"▓"},{"coord":{"x":62,"y":-1},"type":"█"},{"coord":{"x":63,"y":-1},"type":"█"},{"coord":{"x":64,"y":-1},"type":"█"},{"coord":{"x":65,"y":-1},"type":"█"},{"coord":{"x":66,"y":-1},"type":"█"},{"coord":{"x":67,"y":-1},"type":"█"},{"coord":{"x":68,"y":-1},"type":"█"},{"coord":{"x":69,"y":-1},"type":"█"},{"coord":{"x":70,"y":-1},"type":"█"},{"coord":{"x":71,"y":-1},"type":"█"},{"coord":{"x":72,"y":-1},"type":"█"},{"coord":{"x":73,"y":-1},"type":"█"},{"coord":{"x":-7,"y":-2},"type":"█"},{"coord":{"x":-6,"y":-2},"type":"█"},{"coord":{"x":-5,"y":-2},"type":"█"},{"coord":{"x":-4,"y":-2},"type":"█"},{"coord":{"x":-3,"y":-2},"type":"█"},{"coord":{"x":-2,"y":-2},"type":"█"},{"coord":{"x":-1,"y":-2},"type":"█"},{"coord":{"x":0,"y":-2},"type":"█"},{"coord":{"x":1,"y":-2},"type":"█"},{"coord":{"x":2,"y":-2},"type":"█"},{"coord":{"x":3,"y":-2},"type":"█"},{"coord":{"x":4,"y":-2},"type":"█"},{"coord":{"x":5,"y":-2},"type":"█"},{"coord":{"x":6,"y":-2},"type":"█"},{"coord":{"x":7,"y":-2},"type":"█"},{"coord":{"x":8,"y":-2},"type":"█"},{"coord":{"x":9,"y":-2},"type":"█"},{"coord":{"x":10,"y":-2},"type":"█"},{"coord":{"x":11,"y":-2},"type":"█"},{"coord":{"x":12,"y":-2},"type":"█"},{"coord":{"x":13,"y":-2},"type":"█"},{"coord":{"x":14,"y":-2},"type":"█"},{"coord":{"x":15,"y":-2},"type":"█"},{"coord":{"x":16,"y":-2},"type":"█"},{"coord":{"x":46,"y":-2},"type":"*"},{"coord":{"x":47,"y":-2},"type":"*"},{"coord":{"x":48,"y":-2},"type":"*"},{"coord":{"x":49,"y":-2},"type":"*"},{"coord":{"x":50,"y":-2},"type":"*"},{"coord":{"x":51,"y":-2},"type":"*"},{"coord":{"x":52,"y":-2},"type":"*"}
        ]
    ]
    map = copy.deepcopy(maps[map_num])

    p = {"name": user_info["name"][0].upper(), "x_pos": 0, "y_pos": 0, "x_pos_acc": 0, "y_pos_acc": 0, "x_vel": 0, "y_vel": 0, "coins": 0, "time": 0, "preferences": {"screen_size": user_info["preferences"]}} # All the player’s important values.
    start_time = time.time()

    fallings = []

    while run:
        p = active_move(map, p)  # Physics systems
        p = passive_move(map, p)

        display(map, p) # Display systems
        print(f"Time: {p["time"]}\nCoins: {p["coins"]}/3")


        colls = collision(map, p)
        if 'coin' in colls:
            coin = map.index({"coord":{"x": p["x_pos"], "y": p["y_pos"]},"type":"C"})
            p["coins"] += 1
            del map[coin]
        if 'lever' in colls:
            try:
                lever = next(
                (i for i, d in enumerate(map) if all(item in d.items() for item in {"coord":{"x": p["x_pos"], "y": p["y_pos"]},"type":"/"}.items())),
                None
                )
                for coord in map[lever]["door"]:
                    door = map.index({"coord":coord,"type":"|"})
                    del map[door]
            except:
                pass
        
        if 'falling' in colls:
            thread = threading.Thread(target=falling_block, args=(p, fallings), daemon=True)
            thread.start()

        if 'dead' in colls:
            os.system("cls")
            action = inquirer.select(
                message="You've died!",
                choices=[
                    "Retry",
                    "Main Menu"
                    ],
                default=None,
            ).execute()
            match action:
                case "Retry":
                    map = copy.deepcopy(maps[map_num])
                    p = {"name": user_info["name"][0].upper(), "x_pos": 0, "y_pos": 0, "x_pos_acc": 0, "y_pos_acc": 0, "x_vel": 0, "y_vel": 0, "coins": 0, "time": 0, "preferences": {"screen_size": user_info["preferences"]}} # All the player’s important values.
                    start_time = time.time()
                case "Main Menu":
                    return user_info, level_scores
                
        if 'fin' in colls:
            print(f"Congratulations! You've completed map {map_num + 1} in {p["time"]} seconds with {p["coins"]}/3 coins!")
            user_info = personal_lead(user_info, map_num, [p['time'], p['coins']])
            level_scores = overall_lead(level_scores, map_num, [p['time'], p['coins']])
            if map_num == user_info["unlocked"] and user_info["unlocked"] != 14:
                user_info["unlocked"] += 1
            input("Done reading?: ")
            return user_info, level_scores

        if keyboard.is_pressed("esc"):
            pause_time = time.time()
            while True:
                os.system("cls")
                action = inquirer.select(
                    message="Game paused.",
                    choices=[
                        "Resume",
                        "Retry",
                        "Options",
                        "Main Menu"
                        ],
                    default=None,
                ).execute()

                match action:
                    case "Resume":
                        start_time += (time.time()-pause_time)
                        break
                    case "Retry":
                        map = copy.deepcopy(maps[map_num])
                        p = {"name": user_info["name"][0].upper(), "x_pos": 0, "y_pos": 0, "x_pos_acc": 0, "y_pos_acc": 0, "x_vel": 0, "y_vel": 0, "coins": 0, "time": 0, "preferences": {"screen_size": user_info["preferences"]}} # All the player’s important values.
                        start_time = time.time()
                        break
                    case "Options":
                        while True:
                            os.system("cls")
                            choice = inquirer.select(
                                message='Options',
                                choices=['Screen Size', 'Exit']
                            ).execute()

                            match choice:
                                case "Screen Size":
                                    screen_size = int(inquirer.number(
                                        message="Select screen size:",
                                        min_allowed=10,
                                        max_allowed=30,
                                        validate=EmptyInputValidator(),
                                    ).execute())
                                    p["preferences"]["screen_size"] = screen_size
                                case "Exit":
                                    break
                    case "Main Menu":
                        return user_info, level_scores

        time.sleep(0.05) # Timer systems
        p["time"] = round(time.time()-start_time, 2)