
import os

def area(x1, y1, x2, y2): # Defines a function which takes two coordinate points and selects every point between them.
    area_list = []
    for y in range(y2, y1 - 1, -1):
        for x in range(x1, x2 + 1):
            area_list.append({'x': x, 'y': y}) # Slight modification to allow for dictionaries but otherwise the same.
    return area_list

def get_block(coord, p, map):
    if coord == {'x': p["x_pos"], 'y': p["y_pos"]}:
        return p["name"]
    for block in map:
        if block["coord"] == coord:
            return block["type"]
    return ' '

def display(map, p, user_info): # Displays the screen around the player based on their selected screen size.
    os.system["cls"]
    s = user_info["preferences"]["screen_size"]
    row = []
    prev_Y = 100
    for space in area(p['x_pos'] - s, p['y_pos'] - s, p['x_pos'] + s, p['y_pos'] + s):
        if space["y"] != prev_Y:
            for i in row:
                print(i, end="")
            row = []
        row.append(get_block(space, p, map))
        prev_Y = space["y"]
