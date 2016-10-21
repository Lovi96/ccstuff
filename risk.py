import random
attackTroops = int(input("Number of attacking troops? "))
defendTroops = int(input("Number of defending troops? "))
attackNum1 = random.randrange(1,7)
attackNum2 = random.randrange(1,7)
attackNum3 = random.randrange(1,7)
defendNum1 = random.randrange(1,7)
defendNum2 = random.randrange(1,7)
attackDice = []
defendDice = []
attackDice.append(attackNum1)
attackDice.append(attackNum2)
attackDice.append(attackNum3)
attackDice.sort()
defendDice.append(defendNum1)
defendDice.append(defendNum2)
defendDice.sort()
attackHighest1 = attackDice[2]
attackHighest2 = attackDice[1]
attackHighest3 = attackDice[0]
defendHighest1 = defendDice[1]
defendHighest2 = defendDice[0]
if (attackTroops == 3) and (defendTroops == 2):
    print("Attacker {} -- {} Defender\nAttacker {} -- {} Defender\nAttacker {}".format(attackHighest1,defendHighest1,attackHighest2,defendHighest2,attackHighest3))
    if attackHighest1 > defendHighest1:
        print("Defender loses 1 army")
        if attackHighest2 > defendHighest2:
            print("Defender loses 1 army")
        elif defendHighest2 > attackHighest2:
            print("Attacker loses 1 army")
    elif defendHighest1 > attackHighest1:
        print("Attacker loses 1 army")
        if attackHighest2 > defendHighest2:
            print("Defender loses 1 army")
        elif defendHighest2 > attackHighest2:
            print("Attacker loses 1 army")
    elif (attackHighest1 == defendHighest1) or (attackHighest2 == defendHighest2):
        print("Attacker loses 1 army")