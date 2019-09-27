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

class Weapon(Ability):
    def weapon(self, weapon_max_damage):
        return random.randint(weapon_max_damage//2, weapon_max_damage)

class Hero:
    def __init__(self, name, current_health, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = current_health
        self.armor = list()
        self.abilities = list()
        self.weapons = list()
    def add_ability(self, ability):
        self.abilities.append(ability)
    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    def attack(self):
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
        return damage
    def attack_weapon(self):
        weapon_damage = 0
        for weapon in self.weapons:
            weapon_damage += weapon.weapon()
        return weapon_damage
    def add_armor(self, armor):
        self.armor.append(armor)
    def defend(self):     
        block = 0
        for armor in self.armor:
            block += armor.block()
        return block
    def take_damage(self, damage):
        self.current_health -= damage - self.defend()
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
    def fight(self, opponent):
        while self.current_health and opponent.current_health > 0:
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if len(self.abilities) == 0 and len(opponent.abilities):
            print("Draw")
        elif self.is_alive() == False:
            print(f"{opponent.name} won")
        else:
            print(f"{self.name} won")







if __name__ == "__main__":
#     ability = Ability("debugging activity", 20)
#     print(ability.name)
#     print(ability.attack)
    # print(my_hero.name)
    # print(my_hero.current_health)
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grass Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # # print(hero.abilities)
    # print(hero.attack())
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())
    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 300)
    ability1 = Ability("Super Speed", 10)
    ability2 = Ability("Super Eyes", 10)
    ability3 = Ability("Wizard Wand", 10)
    ability4 = Ability("Wizard Beard", 10)
    weapon1 = Weapon("nuke", 100000000000000000000000000000000000000000000000000000000)
    weapon2 = Weapon("knife", 1)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.add_weapon(weapon2)
    hero2.add_weapon(weapon1)
    hero1.fight(hero2)
