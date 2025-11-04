from .creatcher import Creatcher
import random

class Player(Creatcher):
    def __init__(self,name):
        self.profession = random.choice(["healer","warrior"])
        hp = 50
        if self.profession == "healer":
            hp = 60 
        speed = random.randint(0,5)
        power = random.randint(5,15)
        if self.profession == "warrior":
            power += 2
        armor_rating = random.randint(0,5)
        super().__init__(name,hp,speed,power,armor_rating)
    def speak(self):
        print(f"Hello my name is {self.name} and I am a {self.profession}")
        
    def attack(self,monster,number_dice):
        if monster.armor_rating > self.speed + number_dice:
            print(f"{self.name} missed {monster.name}")
            return False
        else:
            return True
        
        
        
        
        