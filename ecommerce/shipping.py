import random

class Dice:
    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

    print(f"({dice1}, {dice2})")

