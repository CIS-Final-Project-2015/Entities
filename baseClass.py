# Brianna Melius, Zachary Golik, Tyler Kapusniak, Sam Coon
# Character/Monster base class
# 
# The base class to the monsters and characters
import random

class Base(object):
    """ The base class for any character/monster. """
    def __init__(self):
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.xp = xp
        self.level = level
        self.defense = 0
        self.dex = dexterity
        self.str = strength
        self.con = constitution
        self.int = intelligence
        self.wis = wisdom
        self.cha = charisma
        self.AC = armor_class
        self.speed = speed
        self.CMD = CMD
        self.CMB = CMB
        self.Fort = fortitude
        self.Ref = reflex
        self.Will = will
        self.skills = skills
        self.melee = melee
        self.range = ranged
        self.rollOne = rollOne
        self.rollTwo = rollTwo
        self.die = die
        self.damage = damage
        self.damageCrit = damageCrit
        self.str_Mod = __setmods(self.str)
        self.wis_Mod = __setmods(self.wis)
        self.int_Mod = __setmods(self.int)
        self.con_Mod = __setmods(self.con)
        self.dex_Mod = __setmods(self.dex)
        self.cha_Mod = __setmods(self.cha)

    def __setmods(self,attribute, character):
        modifier = 0
        people = character
        if attribute == 0 or attribute == 1 :
            addition = modifier - 5
        elif attribute == 2 or attribute == 3 :
            addition = modifier - 4
        elif attribute == 4 or attribute == 5 :
            addition = modifier - 3
        elif attribute == 6 or attribute == 7 :
            addition = modifier - 2
        elif attribute == 8 or attribute == 9 :
            addition = modifier - 1
        elif attribute == 12 or attribute == 13 :
            addition = modifier + 1
        elif attribute == 14 or attribute == 15 :
            addition = modifier + 2
        elif attribute == 16 or attribute == 17 :
            addition = modifier + 3
        elif attribute == 18 or attribute == 19 :
            addition = modifier + 4
        elif attribute == 20 or attribute == 21 :
            addition = modifier + 5
        elif attribute == 22 or attribute == 23 :
            addition = modifier + 6
        elif attribute == 24 or attribute == 25 :
            addition = modifier + 7
        elif attribute == 26 or attribute == 27 :
            addition = modifier + 8
        elif attribute == 28 or attribute == 29 :
            addition = modifier + 9
        elif attribute == 30 or attribute == 31 :
            addition = modifier + 10
        elif attribute == 32 or attribute == 33 :
            addition = modifier + 11
        elif attribute == 34 or attribute == 35 :
            addition = modifier + 12
        elif attribute == 36 or attribute == 37 :
            addition = modifier + 13
        elif attribute == 38 or attribute == 39 :
            addition = modifier + 14
        elif attribute == 40 or attribute == 41 :
            addition = modifier + 15
        elif attribute == 42 or attribute == 43 :
            addition = modifier + 16

        # if "Morningstar" in Cleric.inventory:
            
        return modifier

    # Attack Method
    def attack(self):
        # checks if character has both ranged and melee weapons
        if melee and ranged > 1:
            # random roll to decide which attack
            attack = random.randint(1, 2)
            # Random Ranged
            if attack == 1:
                roll = random.randint(1, 20)
                attackRoll = (roll + strMod + size)
                if roll == 1:
                    return 0

                elif roll <= 19:
                    # die = number of dice
                    while i < die:
                        rollOne += random.randint(1, dieface)
                        i += 1

                    damage = rollOne + melee
                    return damage

                # crit
                elif roll == 20:
                    while i < die:
                        rollOne += random.randint(1, dieface)
                        i += 1

                    i = 0
                    damage = rollOne + melee
                    while i < die:
                        rollTwo += random.randint(1, dieface)
                        i += 1

                    damageCrit = rollTwo + melee
                    return damage, damageCrit

            # Random Melee
            elif attack == 2:
                roll = random.randint(1, 20)
                attackRoll = (roll + dexMod + size)
                if roll == 1:
                    return False

                elif roll <= 19:
                    # die = number of dice
                    while i < die:
                        rollOne += random.randint(1, dieface)
                        i += 1

                    damage = rollOne + ranged
                    return damage

                # crit
                elif roll == 20:
                    while i < die:
                        rollOne += random.randint(1, dieface)
                        i += 1

                    i = 0
                    damage = rollOne + ranged
                    while i < die:
                        rollTwo += random.randint(1, dieface)
                        i += 1

                    damageCrit = rollTwo + ranged
                    return damage, damageCrit
                
        # If there is only a ranged attack, runs
        if ranged >= 1:
            roll = random.randint(1, 20)
            attackRoll = (roll + dexMod + size)
            if roll == 1:
                return False

            elif roll <= 19:
                #die = number of dice
                while i < die:
                    rollOne += random.randint(1, dieface)
                    i += 1

                damage = rollOne + ranged
                return damage

            # crit
            elif roll == 20:
                while i < die:
                    rollOne += random.randint(1, dieface)
                    i += 1

                i = 0
                damage = rollOne + ranged
                while i < die:
                    rollTwo += random.randint(1, dieface)
                    i += 1

                damageCrit = rollTwo + ranged
                return damage, damageCrit

        # If there is only a melee attack, runs
        elif melee >= 1:
            roll = random.randint(1, 20)
            attackRoll = (roll + strMod + size)
            if roll == 1:
                return False

            elif roll <= 19:
                # die = number of dice
                while i < die:
                    rollOne += random.randint(1, dieface)
                    i += 1

                damage = rollOne + melee
                return damage

            # crit
            elif roll == 20:
                while i < die:
                    rollOne += random.randint(1, dieface)
                    i += 1

                i = 0
                damage = rollOne + melee
                while i < die:
                    rollTwo += random.randint(1, dieface)
                    i += 1

                damageCrit = rollTwo + melee
                return damage, damageCrit
            
    def Rep_HP(self):
        self.base_hp = health    
        # make sure that we import health from character/monster class.
        # Need return from combat
    

    def dying(self):
        self.base_hp = hp
        # checks if character is dead
        if hp <= -5:
            character = ("Dead")
            return character

        else:
            character = ("Alive")
            return character

    
