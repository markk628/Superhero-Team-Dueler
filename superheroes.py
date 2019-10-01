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
    def __init__(self, name, starting_health= 100):
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
    # def attack_weapon(self):
    #     weapon_damage = 0sup
    #     for weapon in self.weapons:
    #         weapon_damage += weapon.attack()
    #     return weapon_damage
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
    def is_dead(self):
        if self.current_health < 0:
            return True
        else:
            return False
    def add_kill(self, num_kills):
        self.kills += num_kills
        # return self.kills
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
        # return self.deaths
    def fight(self, opponent):
        # while self.is_alive() and opponent.is_alive():
        #     self.take_damage(opponent.attack())
        #     opponent.take_damage(self.attack())
        # # if len(self.abilities) == 0 and len(opponent.abilities):
        # #     print("Draw")
        #     if self.is_alive() == False:
        #         self.add_deaths(1)
        #         opponent.add_kill(1)
        #         print(f"{opponent.name} won")
        #     else:
        #         self.add_kill(1)
        #         opponent.add_deaths(1)
        #         print(f"{self.name} won")
        while self.is_alive() and opponent.is_alive() :
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if self.is_alive() is False:
                self.add_deaths(1)
                opponent.add_kill(1)
                # return print(f"{opponent.name} won")
            elif opponent.is_alive() is False:
                self.add_kill(1)
                opponent.add_deaths(1)
                # return print(f"{self.name} won")

class Team:
    def __init__(self, name, starting_health=100):
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
        random_hero = random.choice(self.heroes)
        other_random_hero = random.choice(other_team.heroes)
        while random_hero.is_alive() and other_random_hero.is_alive():
            random_hero.fight(other_random_hero)

        # while len(self.currently_alive()) > 0 and len(other_team.currently_alive()) > 0:
        #     hero = random.choice(self.currently_alive())
        #     opponent = random.choice(other_team.currently_alive())
        #     hero.fight(opponent)
        #     print("attack method")

        # if self.currently_alive() and other_team.currently_alive():
        #     hero1 = self.heroes[random.randint(0, (len(self.heroes))-1)]
        #     hero2 = other_team.heroes[random.randint(0, (len(other_team.heroes))-1)]
        #     hero1.fight(hero2)
    def currently_alive(self):
        currently_alive = list()
        for hero in self.heroes:
            if hero.is_alive is True:
                currently_alive.append(hero)
            return currently_alive
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health == health
    def stats(self):
        # kill_death = 0
        # total_kills = 0
        # total_deaths = 0
        # for hero in self.heroes:
        #     total_kills += self.kills
        #     total_deaths += self.deaths
        #     if total_deaths == 0:
        #         kill_death = total_kills
        #     else:
        #         kill_death = total_kills/total_deaths
        # print(hero.name, kill_death)
        for hero in self.heroes:
            print(hero.name, hero.kills, hero.deaths)

class Arena:
    def __init__(self):
        self.team_One = Team("team one")
        self.team_Two = Team("team two")
    def create_ability(self):
        c_ability = input("Ability name: ")
        ability_d = int(input("Ability damage (as an integer): "))
        return Ability(c_ability, ability_d)
    def create_weapon(self):
        c_weapon = input("Weapon name: ")
        weapon_d = int(input("Weapon damage (as an integer): "))
        return Weapon(c_weapon, weapon_d)
    def create_armor(self):
        c_armor = input("Armor name: ")
        armor_r = int(input("Armor rating (as an integer): "))
        return Armor(c_armor, armor_r)
    def create_hero(self):
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
        self.team_o_name = input("Enter Team One's name: ")
        self.team_One = Team(self.team_o_name)
        team_o_heroes = int(input(f"Amount of heroes on {self.team_o_name}: "))
        for i in range(team_o_heroes):
            hero = self.create_hero()
            self.team_One.add_hero(hero)
    def build_team_two(self):
        self.team_t_name = input("Enter Team Two's name: ")
        self.team_Two = Team(self.team_t_name)
        team_t_heroes = int(input(f"Amount of heroes on {self.team_t_name}: "))
        for i in range(team_t_heroes):
            hero = self.create_hero()
            self.team_Two.add_hero(hero)
    def team_battle(self):
        self.team_One.attack(self.team_Two)
    # def who_dead(self, Living):
    #     deaths = 0
    #     for hero in Living:
    #         if hero.currently_alive is False:
    #             deaths += 1
    #     if deaths == len(Living):
    #         return True
    #     else:
    #         return False
    def show_stats(self):
        # team_One = self.who_dead(self.team_One.heroes)
        # team_Two = self.who_dead(self.team_Two.heroes)
        # if team_One == False:
        #     print("Survivors")
        #     for hero in self.team_One.heroes:
        #         if hero.is_alive():
        #             print(hero.name)
        # elif team_Two == False:
        #     print("Survivors")
        #     for hero in self.team_Two.heroes:
        #         if hero.is_alive():
        #             print(hero.name)
        #         else:
        #             print("They all dead lol")
        # else:
        #     print("Tie")
        print("stats (K/D)")
        self.team_One.stats()
        self.team_Two.stats()
        if len(self.team_One.currently_alive()) > 0:
            print(self.team_o_name + " wins")
        else:
            print(self.team_t_name + " wins")
        
if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()

# if __name__ == "__main__":
#    team1 = Team("Super Dupers")
#    other_team = Team("Stompers")
#    hero1 = Hero("Wonder Lady")
#    hero2 = Hero("Water Lady")
#    hero3 = Hero("Wind Lady")
#    other_team_hero1 = Hero("Winter Storm")
#    other_team_hero2 = Hero("Sand Storm")
#    other_team_hero3 = Hero("Tornado")
#    ability1 = Ability("Super Speed", 300)
#    ability2 = Ability("Super Eyes", 130)
#    ability3 = Ability("Wizard Wand", 80)
#    ability4 = Ability("Wizard Beard", 20)
#    hero2.add_ability(ability1)
#    other_team_hero2.add_ability(ability2)
#    hero1.add_ability(ability3)
#    other_team_hero1.add_ability(ability4)
#    other_team.add_hero(other_team_hero1)
#    other_team.add_hero(other_team_hero2)
#    other_team.add_hero(other_team_hero3)
#    team1.add_hero(hero1)
#    team1.add_hero(hero2)
#    team1.add_hero(hero3)
#    team1.attack(other_team)
#    team1.stats()
#    other_team.stats()

# # 2nd test for fight() method
# if __name__ == "__main__":
#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero2.add_ability(ability1)
#     hero2.add_ability(ability2)
#     hero1.add_ability(ability3)
#     hero1.add_ability(ability4)
#     hero1.fight(hero2)
#     print(hero1.deaths)