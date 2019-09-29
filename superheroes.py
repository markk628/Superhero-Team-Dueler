import random
import sys

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
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
        self.armors = list()
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
            weapon_damage += weapon.attack()
        return weapon_damage
    def add_armor(self, armor):
        self.armors.append(armor)
    def defend(self):     
        block = 0
        for armor in self.armors:
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
            self.add_deaths(1)
            opponent.add_kill(1)
            print(f"{opponent.name} won")
        else:
            self.add_kill(1)
            opponent.add_deaths(1)
            print(f"{self.name} won")
    def add_kill(self, num_kills):
        self.kills += num_kills
        return self.kills
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
        return self.deaths

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
    def remove_hero(self, name):
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
                return self.heroes
        return 0
    def view_all_heroes(self):
        for heroes in self.heroes:
            print(heroes.name)
    def add_hero(self, hero):
        self.heroes.append(hero)
    def attack(self, other_team):
        while self.currently_alive() and other_team.currently_alive() is True:
            hero = random.choice(self.currently_alive)
            opponent = random.choice(other_team.currently_alive)
            hero.fight(opponent)
    def currently_alive(self):
        currently_alive = list()
        for hero in self.heroes:
            if hero.is_alive is True:
                currently_alive.append(hero)
                return
            return currently_alive
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health == health
    def stats(self):
        for hero in self.heroes:
            print(hero.name, hero.kills, "/", hero.deaths)

class Arena:
    def __init__(self):
        self.team_One: Team("team one")
        self.team_Two: Team("team two")
        # print(self.team_One)
        # print(self.team_Two)
    def create_ability(self):
        c_ability = input("Ability name: ")
        ability_d = int(input("Ability damage (as an integer): "))
        print(c_ability, ability_d)
    def create_weapon(self):
        c_weapon = input("Weapon name: ")
        weapon_d = int(input("Weapon damage (as an integer): "))
        print(c_weapon, weapon_d)
    def create_armor(self):
        c_armor = input("Armor name: ")
        armor_r = int(input("Armor rating (as an integer): "))
        print(c_armor, armor_r)
    def create_hero(self):
        # create_h = input("Would you like to create a hero (Y/N): ")
        # while create_h.upper() == "Y":
        #     break
        # else:
        #     print("ok")
        #     exit()
        c_hero = input("Hero name: ")
        new_hero = Hero(c_hero)
        a_ability = input("Would you like to add an ability (Y/N)?: ")
        while a_ability.upper() == "Y":
            new_hero.add_ability(self.create_ability())
            a_ability = input("Another one (Y/N)?: ")
        a_armor = input("Would you like to add armor (Y/N)?: ")
        while a_armor.upper() == "Y":
            new_hero.add_armor(self.create_armor())
            a_armor = input("Another one (Y/N)?: ")
        a_weapon = input("Would you like to add a weapon (Y/N)?: ")
        while a_weapon.upper() == "Y":
            new_hero.add_weapon(self.create_weapon())
            a_weapon = input("Another one (Y/N)?: ")
        return new_hero
    def build_team_one(self):
        team_o_name = input("Enter Team One's name: ")
        self.team_o = Team(team_o_name)
        self.team_o_heroes = int(input(f"Amount of heroes on {team_o_name}: "))
        for i in range(self.team_o_heroes):
            hero = self.create_hero()
            self.team_o.add_hero(hero)
    def build_team_two(self):
        team_t_name = input("Enter Team Two's name: ")
        self.team_t = Team(team_t_name)
        self.team_t_heroes = int(input(f"Amount of heroes on {team_t_name}: "))
        for i in range(self.team_t_heroes):
            hero = self.create_hero()
            self.team_o.add_hero(hero)
    def team_battle(self):
        self.team_o.attack(self.team_t)
    def show_stats(self):
        print("stats (K/D): ")
        self.team_o_results = self.team_o.stats()
        self.team_t_results = self.team_t.stats()
        print(self.team_o_results)
        print(self.team_o_heroes)
        print(self.team_t_results)
        print(self.team_t_heroes)

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()






    
# if __name__ == "__main__":
# #     ability = Ability("debugging activity", 20)
# #     print(ability.name)
# #     print(ability.attack)
#     # print(my_hero.name)
#     # print(my_hero.current_health)
#     # ability = Ability("Great Debugging", 50)
#     # another_ability = Ability("Smarty Pants", 90)
#     # hero = Hero("Grass Hopper", 200)
#     # hero.add_ability(ability)
#     # hero.add_ability(another_ability)
#     # # print(hero.abilities)
#     # print(hero.attack())
#     # shield = Armor("Shield", 50)
#     # hero.add_armor(shield)
#     # hero.take_damage(50)
#     # print(hero.current_health)
#     # hero = Hero("Grace Hopper", 200)
#     # hero.take_damage(150)
#     # print(hero.is_alive())
#     # hero.take_damage(15000)
#     # print(hero.is_alive())
#     hero1 = Hero("Wonder Woman", 300)
#     hero2 = Hero("Dumbledore", 300)
#     ability1 = Ability("Super Speed", 1)
#     ability2 = Ability("Super Eyes", 1)
#     ability3 = Ability("Wizard Wand", 1)
#     ability4 = Ability("Wizard Beard", 1)
#     weapon1 = Weapon("nuke", 100000000000000000000000000000000000000000000000000000000)
#     weapon2 = Weapon("knife", 0)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.add_weapon(weapon2)
#     hero2.add_weapon(weapon1)
#     # hero1.fight(hero2)
