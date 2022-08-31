"""
This code is compatible with python 2 and python 3.

To run: If you have a unix terminal, you should be able to run it in the
terminal using

>>> python3 /path/to/file/PS1.py

Otherwise: the following website allows you to run python code:
https://pynative.com/online-python-code-editor-to-execute-python-code/

Copy, paste, and click "Run"
"""

import numpy as np
import collections

class Game():

    def __init__(self, rolls_number):
        self.roll_sets = self.get_rolls(rolls_number)
        self.stats = {"games": rolls_number, "full_houses": 0}

    def get_rolls(self, rolls_number):
        return np.random.rand(rolls_number, 5)

    def play(self):
        full_houses = 0
        for roll_set in self.roll_sets:
            rolls = [int(6 * roll + 1) for roll in roll_set]

            if self.check_full_house(rolls):
                full_houses += 1
        self.stats["full_houses"] = full_houses


    def check_full_house(self, rolls):
        rolls = collections.Counter(rolls)
        if 3 in rolls.values() and 2 in rolls.values():
            return True
        return False

    def check_stats(self):
        probability = self.stats["full_houses"] / float(self.stats["games"])
        return probability

game_1 = Game(100)
game_1.play()
print("Proportion of full houses in 100 rolls:")
print(game_1.check_stats())
game_2 = Game(10000)
game_2.play()
print("Proportion of full houses in 10,000 rolls:")
print(game_2.check_stats())
game_3 = Game(1000000)
game_3.play()
print("Proportion of full houses in 1,000,000 rolls:")
print(game_3.check_stats())




