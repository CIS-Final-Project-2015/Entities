# checks if character has both ranged and melee weapons
        if melee and ranged > 1:
            # random roll to decide which attack
            attack = random.randint(1, 2)
