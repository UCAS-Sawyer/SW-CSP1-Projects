#Sawyer Wood, Final

PlayerGold = 5
Inventory = ["HealthPotion", "SpeedPotion"]
PlayerHealth = 25
PlayerSpeed = 10


def TownCenter():
    print ("You can go to the Shop, the House, the River, or the Dungeon.")
    TownCenterDirection = input("Where do you want to go?\t")
    TownCenterDirection = TownCenterDirection.lower()

    if TownCenterDirection in ["the shop", "the house", "the river", "the dungeon", "stop"]:
        if TownCenterDirection == "the shop":
            Shop()
        if TownCenterDirection == "the house":
            House()
        if TownCenterDirection == "the river":
            River()
        if TownCenterDirection == "the dungeon":
            Dungeon()
        if TownCenterDirection == "stop":
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
                print("You will automatically use this weapon in combat since it is your best one.")
            else:
                print("You do not have enough money")
            
            print(f"Your inventory contains {Inventory} and you have {PlayerGold} gold")

def House():
    print("You walk up the cobblestone pathway to your house. You enter your house and climb the stairs to your room.")
    Rest = input("Do you want to rest?\t")
    Rest = Rest.lower()

    if Rest == "yes":
        print("You rest for a while.")

        PlayerHealth = PlayerHealth + 2
        print("You are well rested(+2 health) and ready for an adventure, so you go back to the town center.")

        TownCenter()
    else:
        print("You decide you want to go back into the town center.")
        TownCenter()

def River():
    print("You walk down the dirt pathway to the river. You hear the gushing of the water even before you see it. The path opens up to a river that is fast but fairly small.")

    if "Water" in Inventory:
        print("You sit there for a while, but there is nothing for you to do here so you decide to leave and walk up the path back to the town center.")
        TownCenter()

    else:
        CollectWaterChoice = input("Do you want to collect water?\t")
        CollectWaterChoice = CollectWaterChoice.lower()

        if CollectWaterChoice == "yes":
            print("You grab your extra flask and you fill it with the crystal clear water.(+Water)")
            Inventory.append("Water")

            print("You enjoy the peace for a bit and then you go back to the town center.")
            TownCenter()
        else:
            print("You stand there for a while, but you decide to head back to the town center.")
            TownCenter()




print("An evil necromancer is living in the old crypt down just out of town. The village has grown worried, so they have picked you to fight him. You have some basic items that they have given you. Good luck.")
print("You walk out of your house, down the cobblestone pathway, to the town center.")
TownCenter()