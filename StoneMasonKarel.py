"""
File: StoneMasonKarel.py
Name: Doris
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will fill each of the column
    """
    while front_is_clear():
        up()
        down()
    up()
    down()


def up():
    """
    Pre-condition: Karel is located at the bottom of the column, facing East
    Post-condition: Karel is located at the top of the column, facing North
    """
    turn_left()
    fill_in()


def fill_in():
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()


def down():
    """
    Pre-condition: Karel is located at the top of the column, facing North
    Post-condition: Karel is located the bottom of the column, facing East
    """
    turn_around()
    fill_in()
    turn_left()
    if front_is_clear():
        for i in range(4):
            move()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
