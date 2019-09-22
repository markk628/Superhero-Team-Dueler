import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    def attack(self):
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, current_health, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = current_health
        self.armor = list()
        self.abilities = list()
    def add_ablitly(self, ability):
        self.abilities.append(ability)
    def attack()

if __name__ == "__main__":
#     ability = Ability("debugging activity", 20)
#     print(ability.name)
#     print(ability.attack)
    # print(my_hero.name)
    # print(my_hero.current_health)
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grass Hopper", 200)
    hero.add_ablitly(ability)
    print(hero.abilities)
    
