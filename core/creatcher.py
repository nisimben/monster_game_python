from abc import ABC, abstractmethod


class Creatcher(ABC):
    def __init__(self, name: str, hp: int, speed: int, power: int, armor_rating: int):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def attack(self, target, number_dice):
        pass


