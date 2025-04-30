import os
import time

def area(x1, y1, x2, y2): # Defines a function which takes two coordinate points and selects every point between them.
    area_list = []
    for y in range(y2, y1 - 1, -1):
        for x in range(x1, x2 + 1):
            area_list.append({'x': x, 'y': y})
    return area_list

def get_block(coord, p, map):
    if coord == {"x": p["x_pos"], "y": p["y_pos"]}:
        return p["name"]
    for block in map:
        if block["coord"] == coord:
            return block["type"]
    return " "

def display(map, p, user_info): # Displays the screen around the player based on their selected screen size.
    os.system("cls")
    s = user_info["preferences"]
    prev_y = p["y_pos"] + s
    row = []
    for space in area(p["x_pos"] - s, p["y_pos"] - s, p["x_pos"] + s, p["y_pos"] + s):
        if space["y"] != prev_y:
            for i in row:
                print(i, end='')
            print()
            row = []
        row.append(get_block(space, p, map))
        prev_y = space["y"]


def collision(map, p):
    collision_returns = []
    if get_block({"x": p["x_pos"], "y": p["y_pos"]}, p, map) in ['<', '>', 'v', '^', '*'] or p["y_pos"] < 50:
        collision_returns.append('dead')
    if get_block({"x": p["x_pos"], "y": p["y_pos"]}, p, map) is 'C':
        collision_returns.append('coin')
        for block in map:
            if block['coord'] == {"x": p["x_pos"], "y": p["y_pos"]}:
                map.remove(block)
    if get_block({"x": p["x_pos"], "y": p["y_pos"]}, p, map) == '/':
        lever = map.index({"coord":{"x": p["x_pos"], "y": p["y_pos"]},"type":"/"})
        for block in map:
            if block['coord'] in map[lever]['door']:
                map.remove(block)
        del map[lever]
            

    if get_block({"x": p["x_pos"], "y": p["y_pos"]-1}, p, map) in ["█", "☐"]:
        collision_returns.append('down')
    if get_block({"x": p["x_pos"], "y": p["y_pos"]+1}, p, map) in ["█", "☐"]:
        collision_returns.append('up')
    if get_block({"x": p["x_pos"]-1, "y": p["y_pos"]}, p, map) in ["█", "☐"]:
        collision_returns.append('left')
    if get_block({"x": p["x_pos"]+1, "y": p["y_pos"]}, p, map) in ["█", "☐"]:
        collision_returns.append('right')

    #IF get_block(block below player, p, map) is a falling block:
    #    Passively wait 0.5 seconds
    #    Remove the block from the map
    #    Passively wait 3 seconds
    return collision_returns, map


def passive_move(map, p):
    if 'down' in collision(map, p):
        if p["y_vel"] < 0:
            p["y_vel"] = 0
    else:
        p["y_vel"] -= 0.01 #UNDECIDED                                                                                                                                                                  ---
    if 'up' in collision(map, p) and p["y_vel"] > 0:
        p["y_vel"] = 0

    if 'left' in collision(map, p) and p["x_vel"] < 0:
        p["x_vel"] = 0
    if 'right' in collision(map, p) and p["x_vel"] > 0:
        p["x_vel"] = 0

    p["x_pos_acc"] += p["x_vel"]
    p["y_pos_acc"] += p["y_vel"]
    p["x_pos"] = round(p["x_pos_acc"])
    p["y_pos"] = round(p["y_pos_acc"])
    return p




maps = [
    [{"coord":{"x":72,"y":19},"type":"█"},{"coord":{"x":72,"y":18},"type":"█"},{"coord":{"x":72,"y":17},"type":"█"},{"coord":{"x":72,"y":16},"type":"█"},{"coord":{"x":63,"y":15},"type":"C"},{"coord":{"x":72,"y":15},"type":"█"},{"coord":{"x":72,"y":14},"type":"█"},{"coord":{"x":52,"y":13},"type":"F"},{"coord":{"x":72,"y":13},"type":"|"},{"coord":{"x":51,"y":12},"type":"█"},{"coord":{"x":52,"y":12},"type":"█"},{"coord":{"x":53,"y":12},"type":"█"},{"coord":{"x":72,"y":12},"type":"█"},{"coord":{"x":73,"y":12},"type":"█"},{"coord":{"x":74,"y":12},"type":"█"},{"coord":{"x":75,"y":12},"type":"█"},{"coord":{"x":85,"y":11},"type":"\\"},{"coord":{"x":-4,"y":10},"type":"█"},{"coord":{"x":-3,"y":10},"type":"█"},{"coord":{"x":-2,"y":10},"type":"█"},{"coord":{"x":-1,"y":10},"type":"█"},{"coord":{"x":0,"y":10},"type":"█"},{"coord":{"x":1,"y":10},"type":"█"},{"coord":{"x":2,"y":10},"type":"█"},{"coord":{"x":3,"y":10},"type":"█"},{"coord":{"x":4,"y":10},"type":"█"},{"coord":{"x":5,"y":10},"type":"█"},{"coord":{"x":6,"y":10},"type":"█"},{"coord":{"x":7,"y":10},"type":"█"},{"coord":{"x":78,"y":10},"type":"█"},{"coord":{"x":79,"y":10},"type":"█"},{"coord":{"x":80,"y":10},"type":"█"},{"coord":{"x":84,"y":10},"type":"█"},{"coord":{"x":85,"y":10},"type":"█"},{"coord":{"x":-4,"y":9},"type":"█"},{"coord":{"x":-3,"y":9},"type":"█"},{"coord":{"x":-2,"y":9},"type":"█"},{"coord":{"x":-1,"y":9},"type":"█"},{"coord":{"x":0,"y":9},"type":"█"},{"coord":{"x":1,"y":9},"type":"█"},{"coord":{"x":2,"y":9},"type":"█"},{"coord":{"x":3,"y":9},"type":"█"},{"coord":{"x":4,"y":9},"type":"█"},{"coord":{"x":5,"y":9},"type":"█"},{"coord":{"x":6,"y":9},"type":"█"},{"coord":{"x":7,"y":9},"type":"█"},{"coord":{"x":-4,"y":8},"type":"█"},{"coord":{"x":-3,"y":8},"type":"█"},{"coord":{"x":6,"y":8},"type":"█"},{"coord":{"x":7,"y":8},"type":"█"},{"coord":{"x":-4,"y":7},"type":"█"},{"coord":{"x":-3,"y":7},"type":"█"},{"coord":{"x":6,"y":7},"type":"█"},{"coord":{"x":7,"y":7},"type":"█"},{"coord":{"x":71,"y":7},"type":"█"},{"coord":{"x":72,"y":7},"type":"█"},{"coord":{"x":73,"y":7},"type":"█"},{"coord":{"x":74,"y":7},"type":"█"},{"coord":{"x":75,"y":7},"type":"█"},{"coord":{"x":76,"y":7},"type":"█"},{"coord":{"x":-4,"y":6},"type":"█"},{"coord":{"x":-3,"y":6},"type":"█"},{"coord":{"x":6,"y":6},"type":"█"},{"coord":{"x":7,"y":6},"type":"█"},{"coord":{"x":40,"y":6},"type":"█"},{"coord":{"x":41,"y":6},"type":"█"},{"coord":{"x":42,"y":6},"type":"█"},{"coord":{"x":43,"y":6},"type":"█"},{"coord":{"x":44,"y":6},"type":"█"},{"coord":{"x":45,"y":6},"type":"█"},{"coord":{"x":46,"y":6},"type":"█"},{"coord":{"x":47,"y":6},"type":"█"},{"coord":{"x":48,"y":6},"type":"█"},{"coord":{"x":49,"y":6},"type":"█"},{"coord":{"x":50,"y":6},"type":"█"},{"coord":{"x":71,"y":6},"type":"█"},{"coord":{"x":-4,"y":5},"type":"█"},{"coord":{"x":-3,"y":5},"type":"█"},{"coord":{"x":6,"y":5},"type":"█"},{"coord":{"x":7,"y":5},"type":"█"},{"coord":{"x":40,"y":5},"type":"v"},{"coord":{"x":41,"y":5},"type":"v"},{"coord":{"x":42,"y":5},"type":"v"},{"coord":{"x":43,"y":5},"type":"v"},{"coord":{"x":44,"y":5},"type":"v"},{"coord":{"x":45,"y":5},"type":"v"},{"coord":{"x":46,"y":5},"type":"v"},{"coord":{"x":47,"y":5},"type":"v"},{"coord":{"x":48,"y":5},"type":"v"},{"coord":{"x":49,"y":5},"type":"v"},{"coord":{"x":50,"y":5},"type":"v"},{"coord":{"x":68,"y":5},"type":"^"},{"coord":{"x":71,"y":5},"type":"█"},{"coord":{"x":-4,"y":4},"type":"█"},{"coord":{"x":-3,"y":4},"type":"█"},{"coord":{"x":6,"y":4},"type":"█"},{"coord":{"x":7,"y":4},"type":"█"},{"coord":{"x":68,"y":4},"type":"█"},{"coord":{"x":69,"y":4},"type":"█"},{"coord":{"x":70,"y":4},"type":"█"},{"coord":{"x":71,"y":4},"type":"█"},{"coord":{"x":-7,"y":3},"type":"█"},{"coord":{"x":-6,"y":3},"type":"█"},{"coord":{"x":-5,"y":3},"type":"█"},{"coord":{"x":-4,"y":3},"type":"█"},{"coord":{"x":-3,"y":3},"type":"█"},{"coord":{"x":28,"y":3},"type":"█"},{"coord":{"x":29,"y":3},"type":"█"},{"coord":{"x":-7,"y":2},"type":"█"},{"coord":{"x":-6,"y":2},"type":"█"},{"coord":{"x":-5,"y":2},"type":"█"},{"coord":{"x":-4,"y":2},"type":"█"},{"coord":{"x":-3,"y":2},"type":"█"},{"coord":{"x":63,"y":2},"type":"█"},{"coord":{"x":64,"y":2},"type":"█"},{"coord":{"x":65,"y":2},"type":"█"},{"coord":{"x":75,"y":2},"type":"C"},{"coord":{"x":-7,"y":1},"type":"█"},{"coord":{"x":24,"y":1},"type":"█"},{"coord":{"x":25,"y":1},"type":"█"},{"coord":{"x":26,"y":1},"type":"█"},{"coord":{"x":53,"y":1},"type":"█"},{"coord":{"x":54,"y":1},"type":"█"},{"coord":{"x":55,"y":1},"type":"█"},{"coord":{"x":60,"y":1},"type":"█"},{"coord":{"x":61,"y":1},"type":"█"},{"coord":{"x":62,"y":1},"type":"█"},{"coord":{"x":74,"y":1},"type":"█"},{"coord":{"x":75,"y":1},"type":"█"},{"coord":{"x":76,"y":1},"type":"█"},{"coord":{"x":-7,"y":0},"type":"█"},{"coord":{"x":-5,"y":0},"type":"C"},{"coord":{"x":12,"y":0},"type":"^"},{"coord":{"x":13,"y":0},"type":"^"},{"coord":{"x":14,"y":0},"type":"^"},{"coord":{"x":19,"y":0},"type":"█"},{"coord":{"x":20,"y":0},"type":"█"},{"coord":{"x":21,"y":0},"type":"█"},{"coord":{"x":22,"y":0},"type":"█"},{"coord":{"x":38,"y":0},"type":"█"},{"coord":{"x":39,"y":0},"type":"█"},{"coord":{"x":40,"y":0},"type":"█"},{"coord":{"x":41,"y":0},"type":"█"},{"coord":{"x":42,"y":0},"type":"█"},{"coord":{"x":43,"y":0},"type":"█"},{"coord":{"x":44,"y":0},"type":"█"},{"coord":{"x":45,"y":0},"type":"█"},{"coord":{"x":46,"y":0},"type":"█"},{"coord":{"x":47,"y":0},"type":"█"},{"coord":{"x":48,"y":0},"type":"█"},{"coord":{"x":49,"y":0},"type":"█"},{"coord":{"x":50,"y":0},"type":"█"},{"coord":{"x":-7,"y":-1},"type":"█"},{"coord":{"x":-6,"y":-1},"type":"█"},{"coord":{"x":-5,"y":-1},"type":"█"},{"coord":{"x":-4,"y":-1},"type":"█"},{"coord":{"x":-3,"y":-1},"type":"█"},{"coord":{"x":-2,"y":-1},"type":"█"},{"coord":{"x":-1,"y":-1},"type":"█"},{"coord":{"x":0,"y":-1},"type":"█"},{"coord":{"x":1,"y":-1},"type":"█"},{"coord":{"x":2,"y":-1},"type":"█"},{"coord":{"x":3,"y":-1},"type":"█"},{"coord":{"x":4,"y":-1},"type":"█"},{"coord":{"x":5,"y":-1},"type":"█"},{"coord":{"x":6,"y":-1},"type":"█"},{"coord":{"x":7,"y":-1},"type":"█"},{"coord":{"x":8,"y":-1},"type":"█"},{"coord":{"x":9,"y":-1},"type":"█"},{"coord":{"x":10,"y":-1},"type":"█"},{"coord":{"x":11,"y":-1},"type":"█"},{"coord":{"x":12,"y":-1},"type":"█"},{"coord":{"x":13,"y":-1},"type":"█"},{"coord":{"x":14,"y":-1},"type":"█"},{"coord":{"x":15,"y":-1},"type":"█"},{"coord":{"x":16,"y":-1},"type":"█"},{"coord":{"x":17,"y":-1},"type":"█"},{"coord":{"x":31,"y":-1},"type":"█"},{"coord":{"x":32,"y":-1},"type":"█"},{"coord":{"x":38,"y":-1},"type":"█"},{"coord":{"x":39,"y":-1},"type":"█"},{"coord":{"x":40,"y":-1},"type":"█"},{"coord":{"x":41,"y":-1},"type":"█"},{"coord":{"x":42,"y":-1},"type":"█"},{"coord":{"x":43,"y":-1},"type":"█"},{"coord":{"x":44,"y":-1},"type":"█"},{"coord":{"x":45,"y":-1},"type":"█"},{"coord":{"x":46,"y":-1},"type":"█"},{"coord":{"x":47,"y":-1},"type":"█"},{"coord":{"x":48,"y":-1},"type":"█"},{"coord":{"x":49,"y":-1},"type":"█"},{"coord":{"x":50,"y":-1},"type":"█"},{"coord":{"x":71,"y":-1},"type":"^"},{"coord":{"x":-7,"y":-2},"type":"█"},{"coord":{"x":-6,"y":-2},"type":"█"},{"coord":{"x":-5,"y":-2},"type":"█"},{"coord":{"x":-4,"y":-2},"type":"█"},{"coord":{"x":-3,"y":-2},"type":"█"},{"coord":{"x":-2,"y":-2},"type":"█"},{"coord":{"x":-1,"y":-2},"type":"█"},{"coord":{"x":0,"y":-2},"type":"█"},{"coord":{"x":1,"y":-2},"type":"█"},{"coord":{"x":2,"y":-2},"type":"█"},{"coord":{"x":3,"y":-2},"type":"█"},{"coord":{"x":4,"y":-2},"type":"█"},{"coord":{"x":5,"y":-2},"type":"█"},{"coord":{"x":6,"y":-2},"type":"█"},{"coord":{"x":7,"y":-2},"type":"█"},{"coord":{"x":8,"y":-2},"type":"█"},{"coord":{"x":9,"y":-2},"type":"█"},{"coord":{"x":10,"y":-2},"type":"█"},{"coord":{"x":11,"y":-2},"type":"█"},{"coord":{"x":12,"y":-2},"type":"█"},{"coord":{"x":13,"y":-2},"type":"█"},{"coord":{"x":14,"y":-2},"type":"█"},{"coord":{"x":15,"y":-2},"type":"█"},{"coord":{"x":16,"y":-2},"type":"█"},{"coord":{"x":17,"y":-2},"type":"█"},{"coord":{"x":34,"y":-2},"type":"*"},{"coord":{"x":35,"y":-2},"type":"*"},{"coord":{"x":36,"y":-2},"type":"*"},{"coord":{"x":68,"y":-2},"type":"█"},{"coord":{"x":69,"y":-2},"type":"█"},{"coord":{"x":70,"y":-2},"type":"█"},{"coord":{"x":71,"y":-2},"type":"█"}]]
map = maps[0]
user_info = {"preferences": 20, "name": "hi"}
p = {"name": user_info["name"][0].upper(), "x_pos": 0, "y_pos": 0, "x_pos_acc": 0, "y_pos_acc": 0, "x_vel": 0, "y_vel": 0} # All the player’s important values.

while True:
    p = passive_move(map, p)
    display(map, p, user_info)
    print(p)
    time.sleep(0.25)
