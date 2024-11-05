#Sawyer Wood, raid character creator.

race = input("What race do you want to be, Human, Elf, Dwarf, or Halfling:\t")
playerclass = input("What class do you want to be, Rouge, Palidin, Ranger, Warrior, or Wizard:\t")
race = race.lower()
playerclass = playerclass.lower()

name = input("What is the name of the character?:\t")

health = 10
strength = 10
dexterity = 10
intellegence = 10

if race == "human":
    health += 2
    strength += 2
    dexterity += 2
    intellegence += 2

elif race == "elf":
    health += 2
    dexterity += 3
    intellegence += 3

elif race == "dwarf":
    health += 4
    strength += 4

elif race == "halfing":
    health += 2
    dexterity += 4
    intellegence += 2

if playerclass == "rouge":
    strength += 1
    dexterity += 4
    intellegence += 3

elif playerclass == "palidin":
    health += 3
    strength += 3
    intellegence += 2

elif playerclass == "ranger":
    health += 1
    strength += 1
    dexterity += 3
    intellegence += 3

elif playerclass == "warrior":
    health += 4
    strength += 4

elif playerclass == "wizard":
    health += 1
    intellegence += 7

print(f"You chose {race} for your race, {playerclass} for you class and your name is {name}. Your stats are\nHealth: {health}\nStrength: {strength}\nDexterity: {dexterity}\nIntelegence: {intellegence}")