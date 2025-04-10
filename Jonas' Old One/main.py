#Jonas Fairchild, Final Project

import random
import time
import copy
import os

try: #Checks if the keyboard is installed and does not run the rest of the program if not.
    import keyboard
    moveError = True
except:
    print("Please install the keyboard by typing 'pip3 install keyboard' into the terminal before playing.")
    moveError = False

if moveError:
    playerName = input('Select a one-character name for your player: ')
    while len(playerName) != 1:
        print('Invalid player name. Try again.')
        playerName = input('Select a one-character name for your player: ')

if moveError:
    while True:
        try:
            screenSize = int(int(input("What do you want your screen size to be? (Higher = buggier): ")) / 2)
            while screenSize not in range(5, 16):
                print("Input out of range. Try again.")
                screenSize = int(int(input("What do you want your screen size to be? (range from 10-30): ")) / 2)
            else:
                break
        except:
            print("Invalid input. Try again.")

if moveError:
    tutorial = input('Would you like a quick tutorial? Y/n: ').lower()
    while True:
        if tutorial == 'y':
            print('''
Use WASD to move. Space does not do anything, just press W.
Press W while on a ▯ tile to read signs.
Press E to open the inventory. Press M to open the map.
All bossfights are optional, but without fighting bosses you won't have the equipment to beat the game. Bosses are marked with an E.
Be prepared to enter combat with a smaller creature at random! This will happen every few minutes.
If you see an I on the map, that means an item is there. You should pick it up!
''')
            input('Done reading?: ')
            break
        elif tutorial == 'n':
            break
        else:
            print('Invalid input. Try again.')
            tutorial = input('Would you like a quick tutorial? Y/n: ').lower()


blockTypes = ['▮', '▯', 'v', '^', '>', '<', 'C', 'E', 'I']

map = [
#Blocks
[20, 121], 0, [21, 121], 0, [22, 121], 0, [23, 121], 0, [24, 121], 0, [25, 121], 0, [26, 121], 0, [27, 121], 0, [28, 121], 0, [29, 121], 0, [30, 121], 0, [31, 121], 0, [20, 120], 0, [31, 120], 0, [20, 119], 0, [31, 119], 0, [20, 118], 0, [31, 118], 0, [20, 117], 0, [31, 117], 0, [20, 116], 0, [31, 116], 0, [20, 115], 0, [31, 115], 0, [20, 114], 0, [31, 114], 0, [20, 113], 0, [31, 113], 0, [20, 112], 0, [31, 112], 0, [20, 111], 0, [21, 111], 0, [22, 111], 0, [23, 111], 0, [24, 111], 0, [27, 111], 0, [28, 111], 0, [29, 111], 0, [30, 111], 0, [31, 111], 0, [20, 110], 0, [31, 110], 0, [20, 109], 0, [30, 109], 0, [31, 109], 0, [20, 108], 0, [27, 108], 0, [28, 108], 0, [29, 108], 0, [30, 108], 0, [31, 108], 0, [20, 107], 0, [31, 107], 0, [20, 106], 0, [27, 106], 0, [28, 106], 0, [31, 106], 0, [20, 105], 0, [24, 105], 0, [26, 105], 0, [29, 105], 0, [31, 105], 0, [20, 104], 0, [29, 104], 0, [31, 104], 0, [20, 103], 0, [29, 103], 0, [31, 103], 0, [20, 102], 0, [29, 102], 0, [31, 102], 0, [20, 101], 0, [26, 101], 0, [29, 101], 0, [31, 101], 0, [32, 101], 0, [33, 101], 0, [34, 101], 0, [35, 101], 0, [36, 101], 0, [37, 101], 0, [38, 101], 0, [39, 101], 0, [40, 101], 0, [41, 101], 0, [20, 100], 0, [41, 100], 0, [20, 99], 0, [41, 99], 0, [20, 98], 0, [41, 98], 0, [20, 97], 0, [21, 97], 0, [22, 97], 0, [23, 97], 0, [24, 97], 0, [41, 97], 0, [20, 96], 0, [41, 96], 0, [20, 95], 0, [25, 95], 0, [34, 95], 0, [41, 95], 0, [20, 94], 0, [39, 94], 0, [41, 94], 0, [20, 93], 0, [29, 93], 0, [33, 93], 0, [35, 93], 0, [41, 93], 0, [20, 92], 0, [26, 92], 0, [41, 92], 0, [0, 91], 0, [1, 91], 0, [2, 91], 0, [3, 91], 0, [4, 91], 0, [5, 91], 0, [6, 91], 0, [7, 91], 0, [8, 91], 0, [9, 91], 0, [10, 91], 0, [11, 91], 0, [12, 91], 0, [13, 91], 0, [14, 91], 0, [15, 91], 0, [16, 91], 0, [17, 91], 0, [18, 91], 0, [19, 91], 0, [20, 91], 0, [28, 91], 0, [30, 91], 0, [41, 91], 0, [0, 90], 0, [41, 90], 0, [0, 89], 0, [41, 89], 0, [0, 88], 0, [2, 88], 0, [4, 88], 0, [6, 88], 0, [8, 88], 0, [25, 88], 0, [41, 88], 0, [0, 87], 0, [1, 87], 0, [2, 87], 0, [14, 87], 0, [41, 87], 0, [0, 86], 0, [11, 86], 0, [22, 86], 0, [23, 86], 0, [41, 86], 0, [0, 85], 0, [19, 85], 0, [22, 85], 0, [24, 85], 0, [28, 85], 0, [29, 85], 0, [30, 85], 0, [39, 85], 0, [40, 85], 0, [41, 85], 0, [0, 84], 0, [41, 84], 0, [0, 83], 0, [7, 83], 0, [8, 83], 0, [13, 83], 0, [15, 83], 0, [22, 83], 0, [23, 83], 0, [24, 83], 0, [25, 83], 0, [34, 83], 0, [41, 83], 0, [0, 82], 0, [6, 82], 0, [7, 82], 0, [9, 82], 0, [10, 82], 0, [16, 82], 0, [18, 82], 0, [21, 82], 0, [22, 82], 0, [41, 82], 0, [-20, 81], 0, [-19, 81], 0, [-18, 81], 0, [-17, 81], 0, [-16, 81], 0, [-15, 81], 0, [-14, 81], 0, [-13, 81], 0, [-12, 81], 0, [-11, 81], 0, [-10, 81], 0, [-9, 81], 0, [-8, 81], 0, [-7, 81], 0, [-6, 81], 0, [-5, 81], 0, [-4, 81], 0, [-3, 81], 0, [-2, 81], 0, [-1, 81], 0, [0, 81], 0, [3, 81], 0, [4, 81], 0, [5, 81], 0, [11, 81], 0, [17, 81], 0, [18, 81], 0, [41, 81], 0, [42, 81], 0, [43, 81], 0, [44, 81], 0, [45, 81], 0, [46, 81], 0, [47, 81], 0, [48, 81], 0, [49, 81], 0, [50, 81], 0, [51, 81], 0, [52, 81], 0, [53, 81], 0, [54, 81], 0, [55, 81], 0, [56, 81], 0, [57, 81], 0, [58, 81], 0, [59, 81], 0, [60, 81], 0, [61, 81], 0, [62, 81], 0, [63, 81], 0, [64, 81], 0, [65, 81], 0, [66, 81], 0, [67, 81], 0, [68, 81], 0, [69, 81], 0, [70, 81], 0, [71, 81], 0, [-20, 80], 0, [3, 80], 0, [11, 80], 0, [21, 80], 0, [22, 80], 0, [23, 80], 0, [24, 80], 0, [25, 80], 0, [26, 80], 0, [27, 80], 0, [28, 80], 0, [29, 80], 0, [30, 80], 0, [37, 80], 0, [71, 80], 0, [-20, 79], 0, [2, 79], 0, [21, 79], 0, [30, 79], 0, [64, 79], 0, [71, 79], 0, [-20, 78], 0, [21, 78], 0, [30, 78], 0, [71, 78], 0, [-20, 77], 0, [-8, 77], 0, [21, 77], 0, [30, 77], 0, [40, 77], 0, [61, 77], 0, [64, 77], 0, [71, 77], 0, [-20, 76], 0, [-10, 76], 0, [-9, 76], 0, [6, 76], 0, [8, 76], 0, [9, 76], 0, [21, 76], 0, [30, 76], 0, [48, 76], 0, [53, 76], 0, [57, 76], 0, [71, 76], 0, [-20, 75], 0, [-1, 75], 0, [0, 75], 0, [5, 75], 0, [6, 75], 0, [7, 75], 0, [9, 75], 0, [19, 75], 0, [20, 75], 0, [21, 75], 0, [30, 75], 0, [36, 75], 0, [49, 75], 0, [71, 75], 0, [-20, 74], 0, [1, 74], 0, [4, 74], 0, [9, 74], 0, [10, 74], 0, [16, 74], 0, [17, 74], 0, [18, 74], 0, [19, 74], 0, [21, 74], 0, [30, 74], 0, [54, 74], 0, [70, 74], 0, [71, 74], 0, [-20, 73], 0, [4, 73], 0, [10, 73], 0, [15, 73], 0, [21, 73], 0, [30, 73], 0, [56, 73], 0, [61, 73], 0, [68, 73], 0, [71, 73], 0, [-20, 72], 0, [-9, 72], 0, [-8, 72], 0, [3, 72], 0, [10, 72], 0, [21, 72], 0, [30, 72], 0, [38, 72], 0, [40, 72], 0, [46, 72], 0, [71, 72], 0, [-20, 71], 0, [-13, 71], 0, [-10, 71], 0, [-5, 71], 0, [-4, 71], 0, [4, 71], 0, [10, 71], 0, [11, 71], 0, [21, 71], 0, [30, 71], 0, [51, 71], 0, [57, 71], 0, [71, 71], 0, [-20, 70], 0, [-17, 70], 0, [-14, 70], 0, [-13, 70], 0, [-10, 70], 0, [-3, 70], 0, [-2, 70], 0, [-1, 70], 0, [0, 70], 0, [4, 70], 0, [5, 70], 0, [11, 70], 0, [21, 70], 0, [30, 70], 0, [31, 70], 0, [32, 70], 0, [33, 70], 0, [34, 70], 0, [35, 70], 0, [36, 70], 0, [37, 70], 0, [38, 70], 0, [39, 70], 0, [40, 70], 0, [64, 70], 0, [71, 70], 0, [-20, 69], 0, [-17, 69], 0, [-14, 69], 0, [-10, 69], 0, [1, 69], 0, [2, 69], 0, [5, 69], 0, [11, 69], 0, [21, 69], 0, [40, 69], 0, [47, 69], 0, [50, 69], 0, [57, 69], 0, [71, 69], 0, [-20, 68], 0, [-19, 68], 0, [-17, 68], 0, [-16, 68], 0, [-15, 68], 0, [-14, 68], 0, [-10, 68], 0, [11, 68], 0, [21, 68], 0, [40, 68], 0, [66, 68], 0, [71, 68], 0, [-20, 67], 0, [-16, 67], 0, [-10, 67], 0, [7, 67], 0, [8, 67], 0, [9, 67], 0, [10, 67], 0, [15, 67], 0, [21, 67], 0, [40, 67], 0, [45, 67], 0, [46, 67], 0, [63, 67], 0, [71, 67], 0, [-20, 66], 0, [-16, 66], 0, [-9, 66], 0, [4, 66], 0, [5, 66], 0, [6, 66], 0, [9, 66], 0, [10, 66], 0, [15, 66], 0, [21, 66], 0, [40, 66], 0, [59, 66], 0, [62, 66], 0, [71, 66], 0, [-20, 65], 0, [-17, 65], 0, [-16, 65], 0, [-9, 65], 0, [0, 65], 0, [1, 65], 0, [5, 65], 0, [14, 65], 0, [15, 65], 0, [21, 65], 0, [40, 65], 0, [52, 65], 0, [53, 65], 0, [59, 65], 0, [71, 65], 0, [-20, 64], 0, [-9, 64], 0, [-1, 64], 0, [5, 64], 0, [14, 64], 0, [21, 64], 0, [40, 64], 0, [43, 64], 0, [62, 64], 0, [71, 64], 0, [-20, 63], 0, [-19, 63], 0, [-10, 63], 0, [5, 63], 0, [11, 63], 0, [14, 63], 0, [15, 63], 0, [21, 63], 0, [40, 63], 0, [49, 63], 0, [50, 63], 0, [66, 63], 0, [67, 63], 0, [71, 63], 0, [-20, 62], 0, [-10, 62], 0, [6, 62], 0, [10, 62], 0, [11, 62], 0, [15, 62], 0, [21, 62], 0, [40, 62], 0, [54, 62], 0, [55, 62], 0, [56, 62], 0, [57, 62], 0, [58, 62], 0, [65, 62], 0, [70, 62], 0, [71, 62], 0, [-20, 61], 0, [-14, 61], 0, [-13, 61], 0, [-12, 61], 0, [-9, 61], 0, [-8, 61], 0, [-3, 61], 0, [-2, 61], 0, [-1, 61], 0, [6, 61], 0, [10, 61], 0, [15, 61], 0, [16, 61], 0, [21, 61], 0, [30, 61], 0, [31, 61], 0, [32, 61], 0, [33, 61], 0, [34, 61], 0, [35, 61], 0, [36, 61], 0, [37, 61], 0, [38, 61], 0, [39, 61], 0, [40, 61], 0, [41, 61], 0, [42, 61], 0, [43, 61], 0, [44, 61], 0, [45, 61], 0, [46, 61], 0, [52, 61], 0, [64, 61], 0, [71, 61], 0, [-20, 60], 0, [-14, 60], 0, [-12, 60], 0, [-11, 60], 0, [-7, 60], 0, [-6, 60], 0, [-5, 60], 0, [-4, 60], 0, [0, 60], 0, [7, 60], 0, [16, 60], 0, [21, 60], 0, [30, 60], 0, [37, 60], 0, [64, 60], 0, [71, 60], 0, [-20, 59], 0, [-19, 59], 0, [-18, 59], 0, [-17, 59], 0, [-14, 59], 0, [-11, 59], 0, [-10, 59], 0, [-8, 59], 0, [0, 59], 0, [7, 59], 0, [16, 59], 0, [21, 59], 0, [30, 59], 0, [37, 59], 0, [38, 59], 0, [49, 59], 0, [56, 59], 0, [64, 59], 0, [71, 59], 0, [-20, 58], 0, [-14, 58], 0, [-13, 58], 0, [-8, 58], 0, [1, 58], 0, [7, 58], 0, [21, 58], 0, [30, 58], 0, [38, 58], 0, [42, 58], 0, [56, 58], 0, [59, 58], 0, [64, 58], 0, [67, 58], 0, [71, 58], 0, [-20, 57], 0, [-12, 57], 0, [1, 57], 0, [7, 57], 0, [21, 57], 0, [30, 57], 0, [38, 57], 0, [67, 57], 0, [71, 57], 0, [-20, 56], 0, [-5, 56], 0, [1, 56], 0, [3, 56], 0, [4, 56], 0, [7, 56], 0, [8, 56], 0, [21, 56], 0, [30, 56], 0, [32, 56], 0, [33, 56], 0, [38, 56], 0, [52, 56], 0, [66, 56], 0, [71, 56], 0, [-20, 55], 0, [-16, 55], 0, [1, 55], 0, [4, 55], 0, [8, 55], 0, [13, 55], 0, [21, 55], 0, [30, 55], 0, [33, 55], 0, [39, 55], 0, [40, 55], 0, [41, 55], 0, [49, 55], 0, [53, 55], 0, [57, 55], 0, [71, 55], 0, [-20, 54], 0, [1, 54], 0, [11, 54], 0, [12, 54], 0, [14, 54], 0, [21, 54], 0, [30, 54], 0, [33, 54], 0, [42, 54], 0, [44, 54], 0, [45, 54], 0, [46, 54], 0, [54, 54], 0, [61, 54], 0, [71, 54], 0, [-20, 53], 0, [-11, 53], 0, [-3, 53], 0, [1, 53], 0, [21, 53], 0, [30, 53], 0, [34, 53], 0, [36, 53], 0, [37, 53], 0, [42, 53], 0, [51, 53], 0, [54, 53], 0, [65, 53], 0, [66, 53], 0, [71, 53], 0, [-20, 52], 0, [-19, 52], 0, [-13, 52], 0, [1, 52], 0, [20, 52], 0, [21, 52], 0, [30, 52], 0, [32, 52], 0, [35, 52], 0, [38, 52], 0, [40, 52], 0, [42, 52], 0, [50, 52], 0, [54, 52], 0, [71, 52], 0, [-20, 51], 0, [-19, 51], 0, [-18, 51], 0, [1, 51], 0, [11, 51], 0, [12, 51], 0, [17, 51], 0, [18, 51], 0, [19, 51], 0, [21, 51], 0, [30, 51], 0, [31, 51], 0, [38, 51], 0, [40, 51], 0, [43, 51], 0, [71, 51], 0, [-20, 50], 0, [-19, 50], 0, [-18, 50], 0, [-17, 50], 0, [-16, 50], 0, [-15, 50], 0, [-14, 50], 0, [-13, 50], 0, [-12, 50], 0, [-11, 50], 0, [-10, 50], 0, [-7, 50], 0, [1, 50], 0, [10, 50], 0, [13, 50], 0, [14, 50], 0, [15, 50], 0, [16, 50], 0, [21, 50], 0, [30, 50], 0, [38, 50], 0, [40, 50], 0, [43, 50], 0, [51, 50], 0, [52, 50], 0, [53, 50], 0, [54, 50], 0, [55, 50], 0, [56, 50], 0, [57, 50], 0, [58, 50], 0, [59, 50], 0, [60, 50], 0, [61, 50], 0, [62, 50], 0, [63, 50], 0, [64, 50], 0, [65, 50], 0, [66, 50], 0, [67, 50], 0, [68, 50], 0, [69, 50], 0, [70, 50], 0, [71, 50], 0, [-10, 49], 0, [0, 49], 0, [1, 49], 0, [10, 49], 0, [21, 49], 0, [30, 49], 0, [34, 49], 0, [35, 49], 0, [39, 49], 0, [42, 49], 0, [43, 49], 0, [46, 49], 0, [50, 49], 0, [51, 49], 0, [-10, 48], 0, [0, 48], 0, [5, 48], 0, [6, 48], 0, [7, 48], 0, [10, 48], 0, [21, 48], 0, [30, 48], 0, [34, 48], 0, [38, 48], 0, [42, 48], 0, [45, 48], 0, [46, 48], 0, [49, 48], 0, [51, 48], 0, [-10, 47], 0, [-1, 47], 0, [0, 47], 0, [11, 47], 0, [21, 47], 0, [30, 47], 0, [33, 47], 0, [38, 47], 0, [42, 47], 0, [48, 47], 0, [51, 47], 0, [-10, 46], 0, [0, 46], 0, [11, 46], 0, [21, 46], 0, [30, 46], 0, [37, 46], 0, [42, 46], 0, [48, 46], 0, [51, 46], 0, [-10, 45], 0, [0, 45], 0, [21, 45], 0, [30, 45], 0, [37, 45], 0, [42, 45], 0, [43, 45], 0, [51, 45], 0, [-10, 44], 0, [0, 44], 0, [1, 44], 0, [21, 44], 0, [30, 44], 0, [31, 44], 0, [37, 44], 0, [43, 44], 0, [51, 44], 0, [-10, 43], 0, [-3, 43], 0, [1, 43], 0, [21, 43], 0, [30, 43], 0, [31, 43], 0, [37, 43], 0, [43, 43], 0, [51, 43], 0, [-10, 42], 0, [1, 42], 0, [21, 42], 0, [30, 42], 0, [31, 42], 0, [32, 42], 0, [33, 42], 0, [34, 42], 0, [35, 42], 0, [37, 42], 0, [43, 42], 0, [46, 42], 0, [47, 42], 0, [51, 42], 0, [-10, 41], 0, [0, 41], 0, [1, 41], 0, [21, 41], 0, [22, 41], 0, [23, 41], 0, [24, 41], 0, [25, 41], 0, [26, 41], 0, [27, 41], 0, [28, 41], 0, [29, 41], 0, [30, 41], 0, [38, 41], 0, [44, 41], 0, [46, 41], 0, [51, 41], 0, [-10, 40], 0, [-9, 40], 0, [-8, 40], 0, [-7, 40], 0, [-6, 40], 0, [-5, 40], 0, [-4, 40], 0, [-3, 40], 0, [-2, 40], 0, [-1, 40], 0, [0, 40], 0, [1, 40], 0, [2, 40], 0, [3, 40], 0, [4, 40], 0, [5, 40], 0, [6, 40], 0, [7, 40], 0, [8, 40], 0, [9, 40], 0, [10, 40], 0, [27, 40], 0, [39, 40], 0, [43, 40], 0, [44, 40], 0, [46, 40], 0, [50, 40], 0, [51, 40], 0, [10, 39], 0, [11, 39], 0, [12, 39], 0, [13, 39], 0, [26, 39], 0, [27, 39], 0, [35, 39], 0, [36, 39], 0, [39, 39], 0, [40, 39], 0, [43, 39], 0, [51, 39], 0, [10, 38], 0, [11, 38], 0, [25, 38], 0, [26, 38], 0, [34, 38], 0, [35, 38], 0, [40, 38], 0, [43, 38], 0, [51, 38], 0, [10, 37], 0, [13, 37], 0, [14, 37], 0, [24, 37], 0, [34, 37], 0, [40, 37], 0, [43, 37], 0, [47, 37], 0, [51, 37], 0, [10, 36], 0, [13, 36], 0, [14, 36], 0, [34, 36], 0, [39, 36], 0, [43, 36], 0, [44, 36], 0, [47, 36], 0, [48, 36], 0, [51, 36], 0, [10, 35], 0, [12, 35], 0, [13, 35], 0, [18, 35], 0, [34, 35], 0, [39, 35], 0, [44, 35], 0, [48, 35], 0, [49, 35], 0, [51, 35], 0, [10, 34], 0, [12, 34], 0, [18, 34], 0, [19, 34], 0, [33, 34], 0, [34, 34], 0, [39, 34], 0, [40, 34], 0, [45, 34], 0, [49, 34], 0, [51, 34], 0, [10, 33], 0, [19, 33], 0, [32, 33], 0, [33, 33], 0, [40, 33], 0, [41, 33], 0, [45, 33], 0, [48, 33], 0, [51, 33], 0, [10, 32], 0, [40, 32], 0, [48, 32], 0, [51, 32], 0, [10, 31], 0, [40, 31], 0, [48, 31], 0, [51, 31], 0, [10, 30], 0, [19, 30], 0, [20, 30], 0, [21, 30], 0, [22, 30], 0, [23, 30], 0, [24, 30], 0, [25, 30], 0, [26, 30], 0, [27, 30], 0, [28, 30], 0, [29, 30], 0, [30, 30], 0, [39, 30], 0, [40, 30], 0, [41, 30], 0, [42, 30], 0, [43, 30], 0, [44, 30], 0, [45, 30], 0, [46, 30], 0, [47, 30], 0, [48, 30], 0, [49, 30], 0, [50, 30], 0, [51, 30], 0, [10, 29], 0, [15, 29], 0, [16, 29], 0, [17, 29], 0, [41, 29], 0, [10, 28], 0, [41, 28], 0, [10, 27], 0, [34, 27], 0, [41, 27], 0, [10, 26], 0, [33, 26], 0, [34, 26], 0, [41, 26], 0, [10, 25], 0, [12, 25], 0, [13, 25], 0, [14, 25], 0, [26, 25], 0, [33, 25], 0, [34, 25], 0, [35, 25], 0, [41, 25], 0, [10, 24], 0, [33, 24], 0, [35, 24], 0, [41, 24], 0, [10, 23], 0, [32, 23], 0, [33, 23], 0, [35, 23], 0, [40, 23], 0, [41, 23], 0, [10, 22], 0, [32, 22], 0, [35, 22], 0, [40, 22], 0, [41, 22], 0, [10, 21], 0, [17, 21], 0, [18, 21], 0, [19, 21], 0, [20, 21], 0, [21, 21], 0, [32, 21], 0, [35, 21], 0, [36, 21], 0, [39, 21], 0, [40, 21], 0, [41, 21], 0, [10, 20], 0, [30, 20], 0, [31, 20], 0, [32, 20], 0, [33, 20], 0, [34, 20], 0, [35, 20], 0, [36, 20], 0, [37, 20], 0, [38, 20], 0, [39, 20], 0, [40, 20], 0, [41, 20], 0, [10, 19], 0, [29, 19], 0, [30, 19], 0, [10, 18], 0, [11, 18], 0, [12, 18], 0, [28, 18], 0, [29, 18], 0, [10, 17], 0, [28, 17], 0, [10, 16], 0, [28, 16], 0, [10, 15], 0, [24, 15], 0, [25, 15], 0, [26, 15], 0, [27, 15], 0, [28, 15], 0, [10, 14], 0, [12, 14], 0, [13, 14], 0, [14, 14], 0, [23, 14], 0, [24, 14], 0, [10, 13], 0, [11, 13], 0, [12, 13], 0, [13, 13], 0, [14, 13], 0, [15, 13], 0, [16, 13], 0, [22, 13], 0, [23, 13], 0, [10, 12], 0, [21, 12], 0, [22, 12], 0, [0, 11], 0, [1, 11], 0, [2, 11], 0, [3, 11], 0, [4, 11], 0, [5, 11], 0, [6, 11], 0, [7, 11], 0, [8, 11], 0, [9, 11], 0, [10, 11], 0, [21, 11], 0, [0, 10], 0, [21, 10], 0, [0, 9], 0, [17, 9], 0, [18, 9], 0, [19, 9], 0, [20, 9], 0, [21, 9], 0, [0, 8], 0, [19, 8], 0, [21, 8], 0, [0, 7], 0, [19, 7], 0, [21, 7], 0, [0, 6], 0, [21, 6], 0, [0, 5], 0, [13, 5], 0, [14, 5], 0, [15, 5], 0, [21, 5], 0, [0, 4], 0, [20, 4], 0, [21, 4], 0, [0, 3], 0, [21, 3], 0, [0, 2], 0, [3, 2], 0, [4, 2], 0, [5, 2], 0, [6, 2], 0, [7, 2], 0, [21, 2], 0, [0, 1], 0, [2, 1], 0, [3, 1], 0, [4, 1], 0, [5, 1], 0, [6, 1], 0, [7, 1], 0, [8, 1], 0, [21, 1], 0, [0, 0], 0, [1, 0], 0, [2, 0], 0, [3, 0], 0, [4, 0], 0, [5, 0], 0, [6, 0], 0, [7, 0], 0, [8, 0], 0, [9, 0], 0, [10, 0], 0, [11, 0], 0, [12, 0], 0, [13, 0], 0, [14, 0], 0, [15, 0], 0, [16, 0], 0, [17, 0], 0, [18, 0], 0, [19, 0], 0, [20, 0], 0, [21, 0], 0,
#Coins
[30, 102], 6, [39, 95], 6, [1, 88], 6, [57, 77], 6, [70, 75], 6, [-16, 69], 6, [62, 65], 6, [-13, 59], 6, [66, 57], 6, [0, 42], 6, [12, 36], 6, [49, 31], 6, [36, 22], 6, [20, 8], 6,
#Spikes
[34, 121], 4, [21, 110], 4, [21, 109], 4, [21, 108], 4, [21, 107], 4, [30, 107], 2, [21, 106], 4, [26, 106], 5, [21, 105], 4, [28, 105], 5, [21, 104], 4, [24, 104], 2, [26, 104], 2, [28, 104], 5, [21, 103], 4, [28, 103], 5, [21, 102], 4, [28, 102], 5, [21, 101], 4, [25, 101], 5, [28, 101], 5, [21, 100], 4, [21, 99], 4, [21, 98], 4, [23, 96], 2, [34, 96], 3, [24, 95], 5, [29, 94], 3, [38, 94], 5, [40, 94], 4, [39, 93], 2, [33, 92], 2, [35, 92], 2, [28, 90], 2, [30, 90], 2, [10, 86], 5, [18, 85], 5, [23, 85], 2, [38, 85], 5, [30, 84], 2, [21, 83], 5, [8, 82], 2, [15, 82], 5, [34, 82], 2, [10, 81], 5, [21, 81], 3, [22, 81], 3, [23, 81], 3, [24, 81], 3, [25, 81], 3, [26, 81], 3, [27, 81], 3, [28, 81], 3, [29, 81], 3, [30, 81], 3, [-9, 77], 5, [60, 77], 5, [63, 77], 5, [65, 77], 4, [-8, 76], 4, [40, 76], 2, [-9, 75], 2, [8, 75], 2, [48, 75], 5, [0, 74], 2, [36, 74], 2, [69, 74], 5, [5, 73], 4, [54, 73], 2, [67, 73], 5, [15, 72], 2, [41, 72], 4, [45, 72], 2, [61, 72], 2, [3, 71], 2, [31, 71], 3, [32, 71], 3, [33, 71], 3, [34, 71], 3, [35, 71], 3, [36, 71], 3, [37, 71], 3, [38, 71], 3, [39, 71], 3, [40, 71], 3, [50, 71], 5, [-4, 70], 2, [41, 70], 4, [51, 70], 2, [57, 70], 2, [-15, 69], 3, [-13, 69], 2, [-9, 69], 4, [-1, 69], 2, [4, 69], 2, [41, 69], 4, [64, 69], 2, [47, 68], 2, [50, 68], 2, [-15, 67], 2, [41, 67], 4, [8, 66], 2, [11, 66], 4, [46, 66], 2, [-8, 65], 4, [6, 65], 2, [-17, 64], 2, [0, 64], 2, [41, 64], 4, [44, 64], 4, [53, 64], 2, [59, 64], 2, [-19, 62], 2, [-9, 62], 3, [-8, 62], 3, [49, 62], 2, [66, 62], 2, [-7, 61], 3, [-6, 61], 3, [-5, 61], 3, [-4, 61], 3, [11, 61], 2, [54, 61], 2, [55, 61], 2, [56, 61], 2, [57, 61], 2, [58, 61], 2, [65, 61], 2, [70, 61], 2, [-8, 60], 5, [6, 60], 2, [15, 60], 2, [45, 60], 2, [-18, 58], 2, [41, 58], 5, [-14, 57], 2, [-13, 57], 2, [-8, 57], 2, [42, 57], 2, [56, 57], 2, [59, 57], 2, [64, 57], 2, [-12, 56], 2, [-6, 56], 5, [-4, 56], 4, [32, 56], 2, [41, 56], 3, [67, 56], 4, [-17, 55], 5, [-5, 55], 2, [7, 55], 5, [32, 55], 2, [42, 55], 3, [46, 55], 3, [48, 55], 5, [-16, 54], 2, [4, 54], 2, [13, 54], 2, [53, 54], 2, [57, 54], 2, [62, 54], 4, [-19, 53], 3, [-10, 53], 4, [-4, 53], 5, [-2, 53], 4, [61, 53], 2, [67, 53], 4, [-18, 52], 3, [-12, 52], 4, [-11, 52], 2, [-3, 52], 2, [34, 52], 2, [49, 52], 5, [-17, 51], 3, [-16, 51], 3, [-15, 51], 3, [-14, 51], 3, [-13, 51], 3, [-12, 51], 3, [-11, 51], 3, [-10, 51], 3, [2, 51], 4, [20, 51], 2, [42, 51], 5, [60, 51], 3, [61, 51], 3, [62, 51], 3, [63, 51], 3, [64, 51], 3, [65, 51], 3, [66, 51], 3, [67, 51], 3, [68, 51], 3, [69, 51], 3, [70, 51], 3, [-8, 50], 5, [-6, 50], 4, [11, 50], 2, [12, 50], 2, [42, 50], 5, [46, 50], 3, [50, 50], 3, [-7, 49], 2, [40, 49], 4, [49, 49], 3, [50, 49], 3, [1, 48], 2, [4, 48], 5, [31, 48], 4, [39, 48], 2, [48, 48], 3, [50, 48], 2, [37, 47], 3, [39, 47], 4, [49, 47], 2, [38, 46], 4, [47, 46], 5, [38, 45], 4, [41, 45], 5, [38, 44], 4, [42, 44], 5, [-4, 43], 5, [-2, 43], 4, [38, 43], 4, [42, 43], 5, [47, 43], 3, [-3, 42], 2, [38, 42], 4, [42, 42], 5, [48, 42], 4, [-9, 41], 3, [-8, 41], 3, [-7, 41], 3, [-6, 41], 3, [-5, 41], 3, [-4, 41], 3, [-3, 41], 3, [-2, 41], 3, [-1, 41], 3, [2, 41], 3, [3, 41], 3, [4, 41], 3, [39, 41], 3, [43, 41], 5, [47, 41], 2, [24, 40], 2, [25, 40], 2, [40, 40], 4, [42, 40], 5, [42, 39], 5, [42, 38], 5, [25, 37], 2, [35, 37], 4, [39, 37], 3, [42, 37], 5, [50, 37], 5, [35, 36], 4, [40, 36], 4, [42, 36], 5, [35, 35], 4, [40, 35], 4, [43, 35], 5, [47, 35], 2, [13, 34], 2, [41, 34], 3, [44, 34], 2, [48, 34], 5, [18, 33], 2, [42, 33], 4, [50, 31], 5, [18, 30], 5, [50, 27], 4, [26, 26], 3, [25, 25], 5, [27, 25], 4, [26, 24], 2, [40, 24], 3, [31, 23], 5, [39, 22], 3, [16, 21], 5, [37, 21], 3, [38, 21], 3, [18, 20], 2, [20, 20], 2, [12, 17], 2, [26, 16], 3, [27, 16], 3, [18, 8], 5, [13, 1], 3, [14, 1], 3, [15, 1], 3, [20, 1], 3,
#Items
[13, 15], 8, "Stone Sword", [39, 56], 8, "Shortsword", [16, 75], 8, "Iron Sword", [39, 86], 8, "Platinum Sword",
#Enemies
[24, 31], 7, 16, [25, 31], 7, 16, [26, 31], 7, 16, [27, 31], 7, 16, [23, 32], 7, 16, [24, 32], 7, 16, [25, 32], 7, 16, [26, 32], 7, 16, [27, 32], 7, 16, [22, 33], 7, 16, [23, 33], 7, 16, [24, 33], 7, 16, [25, 33], 7, 16, [26, 33], 7, 16, [27, 33], 7, 16, [28, 33], 7, 16, [24, 34], 7, 16, [25, 34], 7, 16, [26, 34], 7, 16, [27, 34], 7, 16,
[33, 43], 7, 17, [34, 43], 7, 17, [33, 44], 7, 17, [34, 44], 7, 17,
[55, 63], 7, 19, [56, 63], 7, 19, [57, 63], 7, 19, [55, 64], 7, 19, [56, 64], 7, 19, [57, 64], 7, 19, [55, 65], 7, 19, [56, 65], 7, 19, [57, 65], 7, 19,
[7, 68], 7, 18, [8, 68], 7, 18, [9, 68], 7, 18, [7, 69], 7, 18, [8, 69], 7, 18, [9, 69], 7, 18, [7, 70], 8, 18, [8, 70], 9, 18, [9, 70], 7, 18, [8, 71], 7, 18,
[22, 98], 7, 20, [23, 98], 7, 20, [22, 99], 7, 20, [23, 99], 7, 20,
[27, 112], 7, 21, [29, 112], 7, 21, [27, 113], 7, 21, [29, 113], 7, 21, [28, 114], 7, 21, [26, 115], 7, 21, [27, 115], 7, 21, [28, 115], 7, 21, [29, 115], 7, 21, [30, 115], 7, 21, [28, 116], 7, 21, [27, 117], 7, 21, [28, 117], 7, 21, [29, 117], 7, 21, [27, 118], 7, 21, [29, 118], 7, 21, [27, 119], 7, 21, [28, 119], 7, 21, [29, 119], 7, 21
]
playerPos = [6, 3]
gravity = 0.25
velocity = [0, 0]
mapBoard = '''
▮▮▮▮▮▮▮▮▮▮▮
▮▮▮▮▮ ▮▮▮▮▮
▮▮▮▮▮ ▮▮▮▮▮
▮▮▮▮▮  ▮▮▮▮
▮▮▮    ▮▮▮▮
▮    ▮    ▮
▮    ▮▮   ▮
▮    ▮    ▮
▮▮   ▮  ▮▮▮
▮▮▮▮    ▮▮▮
▮▮▮▮   ▮▮▮▮
▮▮▮▮  ▮▮▮▮▮
▮▮▮  ▮▮▮▮▮▮
▮▮▮▮▮▮▮▮▮▮▮
'''

enemies = [
    # Relatively Easy to Defeat
    ['Shrublike Creature', 25, [['attack', 'Vine Whip', 5], ['defend', 'Root Shield', 5], ['heal', 'Photosynthesize', 8]], 'Small Healing Potion'],
    ['Red-Eyed Rabbit', 30, [['attack', 'Frantic Bite', 8], ['attack', 'Scratch', 5], ['defend', 'Quick Dodge', 4]], 'Small Healing Potion'],
    
    # Slightly Harder
    ['Shark', 50, [['attack', 'Bite', 12], ['attack', 'Tail Whip', 7], ['defend', 'Water Veil', 8]], 'Small Healing Potion'],
    ['Octopus', 55, [['attack', 'Ink Spray', 8], ['attack', 'Tentacle Slap', 10], ['defend', 'Ink Defense', 6]], 'Small Healing Potion'],
    ['Wolf', 60, [['attack', 'Bite', 10], ['attack', 'Howl', 12], ['defend', 'Dodge', 5]], 'Small Healing Potion'],
    ['Skinwalker', 65, [['attack', 'Shape Strike', 12], ['attack', 'Terrifying Form', 10], ['heal', 'Absorb Essence', 12]], 'Small Healing Potion'],
    
    # Moderately Hard
    ['Sentient Cactus', 70, [['attack', 'Spike Shoot', 10], ['defend', 'Hardened Spikes', 10], ['heal', 'Absorb Sunlight', 10]], 'Medium Healing Potion'],
    ['Sandworm', 75, [['attack', 'Burrow Attack', 15], ['defend', 'Sand Veil', 8], ['attack', 'Devour', 20]], 'Medium Healing Potion'],
    ['Waterbender', 80, [['attack', 'Water Blast', 12], ['attack', 'Tidal Strike', 15], ['defend', 'Water Wall', 12], ['heal', 'Aqua Healing', 15]], 'Medium Healing Potion'],
    ['Rock Hurler', 85, [['attack', 'Stone Throw', 15], ['defend', 'Rock Barrier', 12], ['attack', 'Boulder Smash', 18]], 'Medium Healing Potion'],
    
    # Even Harder
    ['Massive Frog', 90, [['attack', 'Tongue Lash', 12], ['attack', 'Body Slam', 18], ['defend', 'Swamp Dodge', 10]], 'Large Healing Potion'],
    ['Mudsucker', 95, [['attack', 'Mud Slap', 14], ['defend', 'Mud Barrier', 12], ['heal', 'Regenerate Slime', 15]], 'Large Healing Potion'],
    
    # Very Hard
    ['Falcon', 100, [['attack', 'Dive Bomb', 15], ['attack', 'Talon Strike', 12], ['defend', 'Soar Away', 10]], 'Large Healing Potion'],
    ['Golem', 110, [['attack', 'Rock Smash', 18], ['defend', 'Stone Armor', 15], ['heal', 'Absorb Earth', 20]], 'Large Healing Potion'],
    
    # Hardest Non-Boss Enemies
    ['Lava Bird', 120, [['attack', 'Fiery Peck', 18], ['attack', 'Wing Flare', 22], ['defend', 'Flame Guard', 15]], 'Elixr of Life'],
    ['Magma Slime', 125, [['attack', 'Lava Splash', 20], ['attack', 'Heat Pulse', 25], ['defend', 'Molten Shell', 18], ['heal', 'Molten Regeneration', 18]], 'Elixr of Life'],
    
    # Minibosses
    ['Grassworm', 120, [['attack', 'Vine Crush', 15], ['defend', 'Leaf Shield', 10], ['heal', 'Regrow', 5]], 'Wooden Shield'],
    ['The Silent One', 130, [['attack', 'Shadow Claw', 22], ['attack', 'Silence Strike', 25], ['defend', 'Shadow Fade', 12]], 'Iron Shield'],
    ['The Sandmaster', 140, [['attack', 'Sandstorm', 28], ['defend', 'Sand Cloak', 15], ['heal', 'Desert Absorption', 25]], 'Steel Shield'],
    ['Skrum', 150, [['attack', 'Tentacle Slam', 30], ['attack', 'Ink Burst', 25], ['defend', 'Abyssal Dodge', 18]], 'Platinum Shield'],
    ['Gust', 135, [['attack', 'Hurricane Strike', 24], ['attack', 'Wind Blade', 20], ['defend', 'Gale Shield', 15], ['heal', 'Whirlwind Regeneration', 20]], 'Platinum Shield'],
    ['Vulcan', 200, [['attack', 'Molten Smash', 35], ['attack', 'Eruption', 40], ['defend', 'Lava Armor', 20], ['heal', 'Core Heat Recovery', 30]], "gameEnd"]
]

health = 100 
coins = 0
inventory = []

def area(x1, y1, x2, y2): #Defines a function which takes two coordinate points and selects every point between them.
    areaList = []
    for y in range(y2, y1 - 1, -1):
        for x in range(x1, x2 + 1):
            areaList.append([x, y])
    return areaList

def displayScreen():
    os.system('cls')
    row = []
    prevY = playerPos[1] + 5
    for space in area(playerPos[0] - screenSize, playerPos[1] - screenSize, playerPos[0] + screenSize, playerPos[1] + screenSize):
        if space[1] != prevY:
            for i in row:
                print(i, end='')
                row = []
            print()
        if space in map and space != playerPos:
            row.append(blockTypes[map[map.index(space) + 1]])
        else:
            row.append(' ')
        if space == playerPos:
            row.append(playerName)
        prevY = space[1]

def collision(): #Checks for objects around the player.
    global coins
    coll_returns = []
    for space in area(playerPos[0] - 1, playerPos[1] - 1, playerPos[0] + 1, playerPos[1] + 1):
        if space in map:
            if blockTypes[map[map.index(space) + 1]] == '▮': #Checks for the direction that blocks are in relative to the player.
                if space == [playerPos[0] - 1, playerPos[1]]:
                    coll_returns.append('a')
                if space == [playerPos[0], playerPos[1] + 1]:
                    coll_returns.append('w')
                if space == [playerPos[0] + 1, playerPos[1]]:
                    coll_returns.append('d')
                if space == [playerPos[0], playerPos[1] - 1]:
                    coll_returns.append('s')
            if blockTypes[map[map.index(space) + 1]] in ['v', '^', '>', '<'] and space == playerPos: #Returns a death if a spike overlaps the player.
                coll_returns.append('dead')
            if blockTypes[map[map.index(space) + 1]] == 'E' and space == playerPos:
                coll_returns.append('enemy')
                coll_returns.append(map[map.index(space) + 2])
            if blockTypes[map[map.index(space) + 1]] == '▯' and space == playerPos:
                coll_returns.append('sign')
                coll_returns.append(map[map.index(space) + 2])
            if blockTypes[map[map.index(space) + 1]] == 'I' and space == playerPos: #If a coin is detected, remove it from the board and add it to the score.
                inventory.append(map[map.index(space) + 2])
                print()
                print(f"Congratulations, you found a {map[map.index(space) + 2]}!")
                del map[map.index(space) + 1]
                del map[map.index(space)]
                time.sleep(2)
                return coll_returns
            if blockTypes[map[map.index(space) + 1]] == 'C' and space == playerPos: #If a coin is detected, remove it from the board and add it to the score.
                coins += 1
                print()
                print("Congratulations, you found a coin!")
                del map[map.index(space) + 1]
                del map[map.index(space)]
                time.sleep(2)
                return coll_returns
    return coll_returns

if moveError:
    def move(): #Defines the movement function based on keys pressed, but only if the keyboard is installed.
        keysPressed = []
        for key in ['w', 'a', 's', 'd']:
            if keyboard.is_pressed(key):
                keysPressed.append(key)
        for key in keysPressed:
            if key in collision():
                del keysPressed[keysPressed.index(key)]
            
        if 'w' in keysPressed and 's' in collision() and 'sign' not in collision():
            velocity[1] = 2
        elif 'w' in collision() and velocity[1] > 0 and 'sign' not in collision():
            velocity[1] = 0
        elif 'w' in keysPressed and 'sign' in collision():
            print()
            print(collision()[collision().index('sign') + 1])
            input("Done reading?: ")
        if 'a' in keysPressed and velocity[0] > -1:
            velocity[0] -= 0.25
        elif 'a' in collision() and velocity[0] < 0:
            velocity[0] = 0
        elif velocity[0] < 0:
            velocity[0] += 0.25
        if 's' in collision() and velocity[1] < 0:
            velocity[1] = 0
            gravity = 0
        else:
            gravity = 0.25
        if 'd' in keysPressed and velocity[0] < 1:
            velocity[0] += 0.25
        elif 'd' in collision() and velocity[0] > 0:
            velocity[0] = 0
        elif velocity[0] > 0:
            velocity[0] -= 0.25
        if not 's' in collision() and velocity[1] > -1:
            velocity[1] -= gravity
        return [playerPos[0] + int(velocity[0]), playerPos[1] + int(velocity[1])]
    
    def playMap(): #A set of other functions collected to do everything needed to run the platformer part.
        if keyboard.is_pressed('e') and not keyboard.is_pressed('m'):
            os.system('cls')
            print(inventory)
        elif keyboard.is_pressed('m') and not keyboard.is_pressed('e'):
            os.system('cls')
            print(mapBoard)
        else:
            displayScreen()
        time.sleep(0.25)

def choices(): #Every item in the game that can be both picked up and used. Gives the action you can do with the item, and what that action does.
    choiceReturns = []
    # Swords (Attack Items)
    if 'Stone Sword' in inventory:
        choiceReturns.append(['Stone Sword', 'attack', 'You swing the Stone Sword with force!', 10])
    if 'Iron Sword' in inventory:
        choiceReturns.append(['Iron Sword', 'attack', 'You slash with the Iron Sword, dealing significant damage!', 15])
    if 'Shortsword' in inventory:
        choiceReturns.append(['Shortsword', 'attack', 'You quickly stab with the Shortsword, a precise strike!', 12])
    if 'Platinum Sword' in inventory:
        choiceReturns.append(['Platinum Sword', 'attack', 'You swing the Platinum Sword, unleashing devastating power!', 25])

    # Shields (Defend Items)
    if 'Wooden Shield' in inventory:
        choiceReturns.append(['Wooden Shield', 'defend', 'You raise the Wooden Shield, blocking incoming damage.', 5])
    if 'Iron Shield' in inventory:
        choiceReturns.append(['Iron Shield', 'defend', 'You brace with the Iron Shield, significantly reducing harm.', 10])
    if 'Steel Shield' in inventory:
        choiceReturns.append(['Steel Shield', 'defend', 'You fortify yourself with the Steel Shield, absorbing heavy blows.', 15])
    if 'Platinum Shield' in inventory:
        choiceReturns.append(['Platinum Shield', 'defend', 'You wield the Platinum Shield, deflecting most attacks.', 20])

    # Healing Potions (Heal Items)
    if 'Small Healing Potion' in inventory:
        choiceReturns.append(['Small Healing Potion', 'heal', 'You drink a Small Healing Potion, feeling a bit better.', 15])
    if 'Medium Healing Potion' in inventory:
        choiceReturns.append(['Medium Healing Potion', 'heal', 'You drink a Medium Healing Potion, regaining health.', 30])
    if 'Large Healing Potion' in inventory:
        choiceReturns.append(['Large Healing Potion', 'heal', 'You consume a Large Healing Potion, restoring substantial health.', 50])
    if 'Elixir of Life' in inventory:
        choiceReturns.append(['Elixir of Life', 'heal', 'You drink the Elixir of Life, fully revitalizing yourself!', 100])

    return choiceReturns

def erase(enemy):
    global map
    for space in area(enemy[0] - 10, enemy[1] - 5, enemy[0] + 10, enemy[1] + 5):
        if space in map:
            if blockTypes[map[map.index(space) + 1]] == 'E':
                del map[map.index(space) + 1]
                del map[map.index(space)]

def combat(enemy): #The combat system for enemies. Takes a specific enemy, lets the user make a choice, does a random action for the enemy, and repeats until someone dies.
    global health
    tempEnemy = copy.deepcopy(enemies[enemy])
    userImmunity = 0
    enemyImmunity = 0
    print(f"Oh no, you encountered a {tempEnemy[0]}!")
    while inventory != []:
        print()
        
        healItems = []
        defItems = []
        attackItems = []
        for item in choices():
            if item[1] == 'heal':
                healItems.append(item[0])
            if item[1] == 'defend':
                defItems.append(item[0])
            if item[1] == 'attack':
                attackItems.append(item[0])
        if attackItems != []:
            print("Attack items:")
        for i in attackItems:
            print(i, end = "\n")
        if defItems != []:
            print("Defense items:")
        for i in defItems:
            print(i, end = "\n")
        if healItems != []:
            print("Healing items:")
        for i in healItems:
            print(i, end = "\n")
        
        print()
        
        print(f"Your health: {health}/100")
        print(f"{tempEnemy[0]} health: {tempEnemy[1]}/{enemies[enemy][1]}") #Displays enemy health

        print()
        
        userAttack = input('What do you want to do?: Use ')
        while userAttack not in inventory:
            print('Invalid choice. Try again.')
            
            print()

            healItems = []
            defItems = []
            attackItems = []
            for item in choices():
                if item[1] == 'heal':
                    healItems.append(item[0])
                if item[1] == 'defend':
                    defItems.append(item[0])
                if item[1] == 'attack':
                    attackItems.append(item[0])
            if attackItems != []:
                print("Attack items:")
            for i in attackItems:
                print(i, end = "\n")
            if defItems != []:
                print("Defense items:")
            for i in defItems:
                print(i, end = "\n")
            if healItems != []:
                print("Healing items:")
            for i in healItems:
                print(i, end = "\n")
        
            print()
        
            print(f"Your health: {health}/100")
            print(f"{tempEnemy[0]} health: {tempEnemy[1]}/{enemies[enemy][1]}") #Displays enemy health
            
            print()
            
            userAttack = input('What do you want to do?: Use ')
        
        os.system('cls')

        for item in choices():
            if item[0] == userAttack:
                print(item[2])
                print()
                if item[1] == 'attack':
                    userImmunity = 0
                    tempEnemy[1] -= (abs(item[3] - enemyImmunity)) #Subtracts the enemy’s health by the damage of the user’s attack.
                elif item[1] == 'defend':
                    userImmunity = item[3]
                elif item[1] == 'heal':
                    userImmunity = 0
                    health += item[3]
                    if health > 100:
                        health = 100
            
        
        if tempEnemy[1] <= 0: #If enemy is dead
            print(f'Congratulations, you defeated the {tempEnemy[0]}!')
            erase(playerPos)
            time.sleep(2)
            try:
                inventory.append(tempEnemy[3])
                return 'survived'
            except:
                return 'survived'
        
        enemyAttack = tempEnemy[2][random.randint(tempEnemy[2].index(tempEnemy[2][0]), tempEnemy[2].index(tempEnemy[2][-1]))] #Subtracts the user’s health by the damage of the enemy’s attack.
        print(f"The {tempEnemy[0]} used {enemyAttack[1]}")
        if enemyAttack[0] == 'attack':
            enemyImmunity = 0
            health -= (abs(enemyAttack[2] - userImmunity))
        elif enemyAttack[0] == 'defend':
            enemyImmunity = enemyAttack[2]
        elif enemyAttack[0] == 'heal':
            enemyImmunity = 0
            tempEnemy[1] += enemyAttack[2]
            if tempEnemy[1] >= enemies[enemy][1]:
                tempEnemy[1] = enemies[enemy][1]


        if health <= 0:
            print(f'Oh no, you were killed by a {tempEnemy[0]}!')
            return 'dead'
    else:
        print("Oh no! You have nothing to fight with!")
        return 'dead'

def zone():
    if playerPos in area(1, 1, 20, 20):
        return "Rolling Hills"
    elif playerPos in area(11, 21, 30, 50) or playerPos in area(21, 11, 40, 80):
        return "Grassy Plains"
    elif playerPos in area(31, 31, 60, 60):
        return "Dark Forest"
    elif playerPos in area(1, 41, 20, 80) or playerPos in area(-9, 61, 10, 90):
        return "Dune Desert"
    elif playerPos in area(-19, 41, 0, 80):
        return "The Ocean"
    elif playerPos in area(11, 71, 40, 100):
        return "Windy Cliffs"
    elif playerPos in area(61, 51, 70, 80):
        return "Rapids"
    elif playerPos in area(41, 61, 60, 80):
        return "Bog Swamp"
    elif playerPos in area(21, 101, 30, 120):
        return "Mt. Doom"
    else:
        return "Nowhere"
    
def zoneEnemies():
    if "Rolling Hills:" in zone():
        return ""
    elif "Grassy Plains" in zone():
        return random.randint(0, 1)
    elif "Ocean" in zone():
        return random.randint(2, 3)
    elif "Dark Forest" in zone():
        return random.randint(4, 5)
    elif "Dune Desert" in zone():
        return random.randint(6, 7)
    elif "Rapids" in zone():
        return random.randint(8, 9)
    elif "Bog Swamp" in zone():
        return random.randint(10, 11)
    elif "Windy Cliffs" in zone():
        return random.randint(12, 13)
    elif "Mt. Doom" in zone():
        return random.randint(14, 15)

prevZone = copy.copy(zone())
while moveError: #The loop that starts running the game. Includes a method of restarting the game on death.
    if prevZone != zone():
        print()
        print(f"Entering new zone! Welcome to: {zone()}!")
        prevZone = copy.copy(zone())
        time.sleep(2)
    move()
    playerPos = move()
    playMap()
    if 'enemy' in collision():
        print(collision()[collision().index('enemy') + 1])
        if 'dead' in combat(collision()[collision().index('enemy') + 1]):
            restartGame = input('Game over. Play again? Y/n: ').lower()
            while True:
                if restartGame == 'n':
                    moveError = False
                    break
                elif restartGame == 'y':
                    playerPos = [6, 3]
                    health = 100
                    prevZone = "Rolling Hills"
                    break
                else:
                    print('Invalid input. Try again.')
                    restartGame = input('Game over. Play again? Y/n: ').lower()
    elif random.randint(1, 100) == 1 and zone() not in ["Nowhere", "Rolling Hills"]:
        if 'dead' in combat(zoneEnemies()):
            restartGame = input('Game over. Play again? Y/n: ').lower()
            while True:
                if restartGame == 'n':
                    moveError = False
                    break
                elif restartGame == 'y':
                    playerPos = [6, 3]
                    health = 100
                    prevZone = "Rolling Hills"
                    break
                else:
                    print('Invalid input. Try again.')
                    restartGame = input('Game over. Play again? Y/n: ').lower()
    if 'dead' in collision():
        restartGame = input('Game over. Play again? Y/n: ').lower()
        while True:
            if restartGame == 'n':
                moveError = False
                break
            elif restartGame == 'y':
                playerPos = [6, 3]
                health = 100
                prevZone = "Rolling Hills"
                break
            else:
                print('Invalid input. Try again.')
                restartGame = input('Game over. Play again? Y/n: ').lower()
    if "gameEnd" in inventory:
        print("Congratulations! You beat the game!")
        break