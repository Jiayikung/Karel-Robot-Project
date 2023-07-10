"""
File: CheckerboardKarel.py
Name: Doris
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karen will fill in beepers as a checkerboard pattern
    """
    put_beeper()
    fill_first_line()
    while front_is_clear():
        if on_beeper():
            move()
            turn_right()
            fill_second_line()
        else:
            move()
            turn_right()
            put_beeper()
            fill_first_line()


def fill_first_line():
    """
    Pre-condition: Karel is located at the left-hand side of the row with "a beeper", facing East
    Post-condition: Karel is located at the left-hand side of the row, facing north
    """
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    back_origin()


def fill_second_line():
    """
    Pre-condition: Karel is located at the left-hand side of the row with "no beeper", facing East
    Post-condition: Karel is located at the left-hand side of the row, facing north
    """
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    back_origin()


def back_origin():
    """
    Pre-condition: Karel is located at the right-hand side of the row, facing East
    Post-condition: Karel is located at the left-hand side of the row, facing north
    """
    turn_around()
    while front_is_clear():
        move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
