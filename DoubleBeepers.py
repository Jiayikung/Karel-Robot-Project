"""
File: DoubleBeepers.py
Name: Doris
-------------------------------
This program shows Karel doubling the number
of beepers in front of him by copying the beeper
pile to the right with doubled beepers first,
moving the new pile back, and going home at last
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beepers()
    move()
    move_beepers_back()
    go_home()


def double_beepers():
   """
   Pre-condition: Karel is at (2,1), right on the beeper and facing East
   Post-condition: Karel is at (2,1) with no beeper and faces East
   """
   while on_beeper():
       pick_beeper()
       move()
       put_beeper()
       put_beeper()
       turn_around()
       move()
       turn_around()


def turn_around():
    turn_left()
    turn_left()


def move_beepers_back():
    """
    Pre-condition: Karel is at (3,1), right on the beeper and facing East
    Post-condition: Karel is at (3,1), facing East
    """
    while on_beeper():
        turn_around()
        pick_beeper()
        move()
        put_beeper()
        turn_around()
        move()


def go_home():
    """
    Pre-condition: Karel is at (3,1) with no beeper and facing East
    Post-condition: Karel is at (1,1), facing East
    """
    while not facing_west():
        turn_around()
    while front_is_clear():
        move()
    turn_around()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
