#Sawyer Wood, Final

PlayerGold = 0
Inventory = ["HealthPotion", "SpeedPotion"]

def TownCenter():
    print ("You can go to the Shop, the House, the River, or the Dungeon.")
    TownCenterDirection = input("Where do you want to go?\t")
    TownCenterDirection = TownCenterDirection.lower()
    if TownCenterDirection in ["the shop", "the house", "the river", "the dungeon", "stop"]:
        if TownCenterDirection == "the shop":
            Shop()
        elif TownCenterDirection == "the house":
            House()
        elif TownCenterDirection == "the river":
            River()
        elif TownCenterDirection == "the dungeon":
            Dungeon()
        elif TownCenterDirection == "stop":
            pass
    else:
        print("That is not an option")
        TownCenter()

def Shop():
    ShopInventory = ["Health potions: 10g", "Speed potions: 15g", "Longsword: 30g"]
    print(f"You enter the old shop and see all the wares on the walls and counters. Welcome worrior we have: {ShopInventory}")
    print(f"You have {PlayerGold} gold.")
    while True:
        DoYouWantToBuy = input("Would you like to buy something?(Yes or No)\t")
        DoYouWantToBuy = DoYouWantToBuy.lower()

        if DoYouWantToBuy == "no":
            print("You leave the shop and go back into the town center")
            TownCenter()
        elif DoYouWantToBuy == "yes":
            WhatDoYouWantToBuy = input("What would you like to buy?\t")
            WhatDoYouWantToBuy = WhatDoYouWantToBuy.lower()

            if WhatDoYouWantToBuy == "health potion" and PlayerGold >= 10:
                print("You baught a health potion.")
                PlayerGold =- 10
                Inventory.append("HealthPotion")
            elif WhatDoYouWantToBuy == "speed potion" and PlayerGold >=15:
                print("You baught a speed potion.")
                PlayerGold =- 15
                Inventory.append("SpeedPotion")
            elif WhatDoYouWantToBuy == "longsword" and PlayerGold >= 30:
                print("You bought a longsword")
                PlayerGold =- 30
                Inventory.insert(0, "Longsword")
            else:
                print("You do not have enough money")
            
            print(f"Your inventory contains {Inventory} and you have {PlayerGold} gold")


print("An evil necromancer is living in the old crypt down just out of town. The village has grown worried, so they have picked you to fight him. You have some basic items that they have given you. Good luck.")
print("You walk out of your house, down the cobblestone pathway, to the town center.")
TownCenter()