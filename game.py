
import random

from core.player import Player
from core.goblin import Goblin
from core.orc import Orc

class Game():
    def __init__(self):
        pass
        
    def start(self):
        show_menu()

def show_menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Play a new game")
        print("0. Exit")

        choice = input("What would you like to do? ")

        if choice == "1":
            start_game() 
        elif choice == "0":
            print("Bye Bye!!")
            break
        else:
            print("Invalid choice, please try again.")

            
def calculate_monster_damage(monster):
    damage = monster.power + roll_dice(6)
    if monster.weapon == "Axe":
        return damage * 1.5
    elif monster.weapon == "Knife":
        return damage * 0.5
    else:
        return damage       

def choose_random_monster():
    return random.choice(["orc", "goblin"])

def battle(player, monster, current_turn):
    
    print("\n=== Battle ===")
    if current_turn == "player":
        player.speak()
        is_attack = player.attack(monster,roll_dice(20))
        if not is_attack:
            current_turn = "monster"
            return current_turn
        sum = player.power + roll_dice(6)
        monster.hp -= sum
        print(f"Monster has been hit for {sum} damage, {monster.type} has {monster.hp} hp left")
        current_turn = "monster"
        return current_turn
    else:
        monster.speak()
        is_attack = monster.attack(player,roll_dice(20))
        if not is_attack:
            current_turn = "player"
            return current_turn
        sum = calculate_monster_damage(monster)
        player.hp -= sum
        print(f"You have been hit for {sum} damage, you have {player.hp} hp left")
        current_turn = "player"
    return current_turn

def roll_dice(sides):
    if sides == 6:
        return random.randint(1,6)
    elif sides == 20:
        return random.randint(1,20)
def choose_turn(player, monster):
    player_dice = roll_dice(6)+player.speed
    monster_dice = roll_dice(6)+monster.speed
    if player_dice >= monster_dice:
        return "player"
    else:
        return "monster"
def get_status(player, monster):
    if player.hp <= 0:
        print(f"You lose , game over you have {player.hp} left")
        return
    elif monster.hp <= 0:
        print(f"The {monster.type} has been killed '{monster.hp}' hp left")
        print("You win")
        return
    else:
        print(f"You have {player.hp} hp left")
        print(f"The {monster.type} has {monster.hp} hp left")
        
    
def start_game():
    print("\n=== Game Start ===")
    player = Player("Nisim")
    monster_type = choose_random_monster()
    if monster_type == "orc":
        monster = Orc("Orc")
    elif monster_type == "goblin":
        monster = Goblin("Goblin")
    turn_player = choose_turn(player,monster)
    while player.hp > 0 and monster.hp > 0:
        turn_player = battle(player, monster, turn_player)
        print("\n=== Round End ===")
        print("current turn:", turn_player)
        get_status(player,monster)
        
    
    