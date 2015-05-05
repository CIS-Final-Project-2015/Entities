# Brianna Melius, Zachary Golik, Tyler Kapusniak, Sam Coon
# Character/Monster base class
# 
# The base class to the monsters and characters
from random import randint

class Base(object):
    """ The base class for any character/monster. """
    def __init__(self, name, xp, rangedAtk, rangedDieNum, rangedDieSide,
                 rangedMod, meleeAtk, meleeDieNum, meleeDieSide, meleeMod,
                 strength, dexterity, constitution, intelligence, wisdom,
                 charisma, size, CMB, CMD, armorClass, fort, ref,
                 will, speed, hp, cr, sprite, weapon, rollOne,
                 rollTwo, die, damage, damageCrit):
        self.name = name
        self.xp = xp
        self.rangedAtk = rangedAtk
        self.rangedDieNum = rangedDieNum
        self.rangedDieSide = rangedDieSide
        self.rangedMod = rangedMod
        self.meleeAtk = meleeAtk
        self.meleeDieNum = meleeDieNum
        self.meleeDieSide = meleeDieSide
        self.meleeMod = meleeMod
        self.str = strength
        self.dex = dexterity
        self.con = constitution
        self.intelligence = intelligence
        self.wis = wisdom
        self.cha = charisma
        self.size = size
        self.CMB = CMB
        self.CMD = CMD
        self.armorClass = armorClass
        self.fort = fort
        self.ref = ref
        self.will = will
        self.speed = speed
        self.hp = hp
        self.cr = cr
        self.sprite = sprite
        self.inventory = []
        self.weapon = weapon
        self.carryCap = self.str * 4
        self.rollOne = rollOne
        self.rollTwo = rollTwo
        self.die = die
        self.damage = damage
        self.damageCrit = damageCrit
        self.initiative = 0
        self.attackRoll = 0
        self.living = True
        

    # Attack Method
    def attack(self):

            
        if self.attackRoll == 1:
            return False

        elif 1 < self.roll < 20:
            # numDie = number of dice rolled
            # typeDie = the number of sides each die has.
            damage = 0
            for i in range(self.weapon.numDie):
                hitRoll = (randint(1, self.weapon.typeDie) + dexMod + size)
                damage += hitRoll
            damage = rollOne + ranged
            if self.weapon.rang <= 10:
                damage1 += (self.str // 5)
                return damage, "melee"
            elif self.weapon.rang >= 11:
                damage2 += (self.dex // 5)
                return damage, "ranged"

        # crit
        elif self.initiative == 20:
            # numDie = number of dice rolled
            # typeDie = the number of sides each die has.
            damage1 = 0
            damage2 = 0
            for i in range(self.weapon.numDie):
                hitRoll1 = (randint(1, self.weapon.typeDie) + dexMod + size)
                damage1 += attackRoll
                hitRoll2 = (randint(1, self.weapon.typeDie) + dexMod + size)
                damage2 += attackRoll
            if self.weapon.rang <= 10:
                damage1 += (self.str // 5)
                return damage1, damage2, "crit melee"
            elif self.weapon.rang >= 11:
                damage2 += (self.dex // 5)
                return damage1, damage2, "crit ranged"          

    def roll_initiative(self):
        """generates a random number between 1-20 + dex"""
        self.initiative = randint(1, 20) + self.dex

    def roll_attackDie(self):
        "generates a random number between 1-20"
        self.attackRoll = randint(1, 20)

    def get_attackRoll(self):
        return self.attackRoll

    def get_initiative(self):
        """returns the number of times attack should be run"""
        return self.initiative
            
    def rep_hp(self, health):
        self.hp = health
        # make sure that we import health from character/monster class.

    def get_hp(self):
        """returns objects health"""
        return self.hp
    

    def dying(self):
        # checks if character is dead
        if self.hp <= -5:
            self.living = False
            return self.living

        else:
            self.living = True
            return self.living
