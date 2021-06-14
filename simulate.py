# Simulate user activity for Windows
# Can trigger Brave Ads

import random
from time import sleep
import pydirectinput
import os


# clear log function
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# main simulate function
def simulate():
    while True:
        # u can change x,y with your screen resolution
        # defined screen resolution
        rand_x = random.randint(2567, 4460)
        rand_x2 = random.randint(2567, 4460)
        rand_y = random.randint(1337, 2986)
        rand_y2 = random.randint(1337, 2986)
        # random generator True/False
        choice = random.choice([True, False])
        choice2 = random.choice([True, False])
        choice3 = random.choice([True, False])
        # random move to xy
        pydirectinput.moveTo(rand_x2, rand_y2)
        if choice:
            # move from current pos
            pydirectinput.move(rand_x, rand_y)
        if choice2:
            print('shift')
            # press down shift key
            pydirectinput.keyDown('shift')
            # random sleep
            sleep(random.randint(1, 2))
            # release shift key
            pydirectinput.keyUp('shift')
        if choice3:
            print('ctrl')
            pydirectinput.keyDown('ctrl')
            sleep(random.randint(1, 2))
            pydirectinput.keyUp('ctrl')
            sleep(20)
            # move to defined xy, then click (notif window)
            pydirectinput.moveTo(2321, 1304)
            print('Click')
            # press left mouse button
            pydirectinput.click()
        print('Sleep')
        sleep(random.randint(25, 35))
        if choice and choice2 and choice3:
            print('Sleep 6m')
            sleep(350)
            cls()


if __name__ == '__main__':
    simulate()
