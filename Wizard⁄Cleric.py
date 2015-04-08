# RPG Character class
# Author: Sam Coon
# Wizard and Cleric for group character creation


import baseClass, random

class Wizard(baseClass.Base):
    def __init__(self):
        super(Wizard).__init__(self)
        #Preset skills
        self.str = 10
        self.dex = 14
        self.con = 12
        self.int = 17
        self.wis = 14
        self.cha = 8
        #Class exclusive
        self.spells = []
        self.spellBook = []
        self.dailylimit = 0
        
        
class Cleric(baseClass.Base):
    def __init__(self):
        super(Cleric).__init__(self)
        #Preset skills
        self.str = 16
        self.dex = 11
        self.con = 14
        self.int = 9
        self.wis = 16
        self.cha = 13
        #Class exclusive
        self.base_spells = []
        self.deity = ""
        self.domains = []
        self.dailyLimit = 0
