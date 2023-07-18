"""
File: CollectNewspaperKarel.py
Name: Doris
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
The mission is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will pick up the beeper and return it to the upper left corner
    """
    pick_up_news()
    return_home()


def pick_up_news():
    """
    Pre-condition: Karel is located at the upper left corner, facing East
    Post-condition: Karel is located at the (3,6), facing East
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def turn_right():
    """
    Karel will turn left 3 times.
    """
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


def return_home():
    """
    Pre-condition: Karel is located at the (3,6), facing East
    Post-condition: Karel is located at the upper left corner, facing East
    """
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    while front_is_clear():
        move()
    turn_around()
    put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
