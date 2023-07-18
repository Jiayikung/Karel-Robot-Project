"""
File: MidpointKarel.py
Name: Doris
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    In order to put a beeper at the mid-point of the 1st street,
    Karen will leave beepers as marks back and forth.

    Karen will always put a beeper when she takes a step forward,
    and keep moving until she touches the wall or reaches another beeper.
    After that, she will turn around directly if she touches the wall
    or turn around and pick up the beeper if she faces the second condition.

    After several loops, Karen will meet the goals.
    """
    put_mark()
    while front_is_clear():
        move()
    turn_around()
    while not on_beeper():
        if front_is_clear():
            move()
        if not on_beeper():
            put_beeper()
            if front_is_clear():
                move()
                while not on_beeper():
                    move()
                pick_beeper()
                turn_around()


def put_mark():
    """
    Once Karen moves one step and there's no beeper, Karen will put a beeper as a mark
    """
    if front_is_clear():
        move()
    if not on_beeper():
        put_beeper()


def turn_around():
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
