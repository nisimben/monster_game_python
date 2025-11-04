import random
from .creatcher import Creatcher
"""
name
hp
type
speed
power
armor_rating
weapon
speak()
attack()


"""
class Goblin(Creatcher):
    def __init__(self, name: str):
        hp = 20
        speed = random.randint(5, 10)
        power = random.randint(5, 10)
        armor_rating = 1
        self.weapon = random.choice(["knife", "Sword", "Axe"])
        self.type = "goblin"
        super().__init__(name, hp, speed, power, armor_rating)

    def speak(self):
        print(f"Hello my name is {self.name} and I am a {self.type}")

    def attack(self, target, number_dice):
        if target.armor_rating > self.speed + number_dice:
            print(f"{self.name} missed {target.name}")
            return False
        else:
            return True