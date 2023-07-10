"""
File: PotholeFilling.py
Name: Doris
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_99()
        go_out()


def go_in():
    """
    pre-condition: Karel is at the upper left of the pothole, facing east
    post-condition: Karel is in the pothole, facing south
    """
    move()
    turn_right()
    move()


def go_out():
    """
    loop consistency
    Un-indent: Shift + tab
    pre-condition: equals to go_in function's post-condition
    post-condition: equals to go_in function's pre-condition
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_right():
    """
    Karel will turn left three times
    """
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    """
    Karel will turn his direction around
    """
    turn_left()
    turn_left()


def put_99():
    """
    Karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
