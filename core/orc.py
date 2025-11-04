import random
from .creatcher import Creatcher  

class Orc(Creatcher):
    def __init__(self, name):
        hp = 50
        speed = random.randint(0, 5)
        power = random.randint(10, 15)
        armor_rating = random.randint(2, 8)
        self.weapon = random.choice(["Knife", "Sword", "Axe"])
        self.type = "orc"
        super().__init__(name, hp, speed, power, armor_rating)

    def speak(self):
        print(f"Hello my name is {self.name} and I am a {self.type}")

    def attack(self, target, number_dice):
        if target.armor_rating > self.speed + number_dice:
            print(f"{self.name} missed {target.name}")
            return False
        else:
            return True