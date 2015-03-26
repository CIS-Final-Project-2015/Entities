# save.py
# Produces a saving throw yo :O
import random
Fort = 4
Reflex = 6
Will = 3

# Fortitude
roll = random.randint(1, 20)
fortRoll = (roll + Fort)
print("Roll", roll)
if roll == 1:
    print("Save misses")

elif fortRoll <= 19:
    # check if it saves
    print("Succesfully saved!")

elif roll == 20:
    print("Succesfully saved!")

# Reflex
roll = random.randint(1, 20)
reflexRoll = (roll + Reflex)
print("Roll", roll)
if roll == 1:
    print("Save misses")

elif reflexRoll <= 19:
    # check if it saves
    print("Succesfully saved!")

elif roll == 20:
    print("Succesfully saved!")

# Will
roll = random.randint(1, 20)
willRoll = (roll + Will)
print("Roll", roll)
if roll == 1:
    print("Save misses")

elif willRoll <= 19:
    # check if it saves
    print("Succesfully saved!")

elif roll == 20:
    print("Succesfully saved!")
