"""
File: Steeplechase.py
Name: Doris
---------------------------------
This program makes Karel across multiple steep obstacles
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    Pre-condition: Karel is on the left side of wall, facing East
    Post-condition: Karel is on the right side
    """
    up()
    cross()
    down()


def up():
    """
    Pre-condition: Karel is on the left side of wall, facing East
    Post-condition: Karel is on the upper left, facing East
    """
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()
    # Top of the wall
    # Post-condition: Karel is on the upper left, facing north
    turn_left()
    while not right_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def cross():
    """
    Pre-condition: Karel is at the upper left, facing North
    Post-condition: Karel is at the upper right, facing South
    """
    # if front_is_clear(), no need to check again
    turn_right()
    move()
    turn_right()


def down():
    """
    Pre-condition: Karel is at the upper right, facing South
    Post-condition: Karel is on the right side of wall, facing East
    """
    while front_is_clear():
        move()
    turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
