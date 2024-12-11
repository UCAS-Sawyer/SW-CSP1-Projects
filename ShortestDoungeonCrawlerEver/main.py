#Sawyer Wood, Final

PlayerGold = 20
Inventory = ["HealthPotion", "Shortsword"]
PlayerHealth = 25
PlayerSpeed = 10
PlayerStrenght = 3

Room3Monster = {
    "Attack" : 3,
    "Health" : 10,
    "Speed" : 9,
    "Reward" : 15
}

def TownCenter():
    print ("\nYou can go to the Shop, the House, the River, or the Dungeon.")
    TownCenterDirection = input("\nWhere do you want to go?(Shop, House, River, Dungeon)\t")
    TownCenterDirection = TownCenterDirection.lower()

    if TownCenterDirection in ["shop", "house", "river", "dungeon", "stop"]:
        if TownCenterDirection == "shop":
            Shop()
        if TownCenterDirection == "house":
            House()
        if TownCenterDirection == "river":
            River()
        if TownCenterDirection == "dungeon":
            DungeonEntrance()
        if TownCenterDirection == "stop":
            print("\nThe End")
    else:
        print("\nThat is not an option")
        TownCenter()

def Shop():
    global PlayerGold

    ShopInventory = ["Health potions: 10g", "Speed potions: 15g", "Longsword: 30g"]
    print(f"\nYou enter the old shop and see all the wares on the walls and counters. Welcome worrior we have: {ShopInventory}")
    print(f"\nYou have {PlayerGold} gold.")
    while True:
        DoYouWantToBuy = input("\nWould you like to buy something?(Yes or No)\t")
        DoYouWantToBuy = DoYouWantToBuy.lower()

        if DoYouWantToBuy == "no":
            print("\nYou leave the shop and go back into the town center")
            TownCenter()
        elif DoYouWantToBuy == "yes":
            WhatDoYouWantToBuy = input("\nWhat would you like to buy?\t")
            WhatDoYouWantToBuy = WhatDoYouWantToBuy.lower()

            if WhatDoYouWantToBuy == "health potion" and PlayerGold >= 10:
                print("\nYou baught a health potion.")
                PlayerGold -= 10
                Inventory.append("HealthPotion")
            elif WhatDoYouWantToBuy == "speed potion" and PlayerGold >=15:
                print("\nYou baught a speed potion.")
                PlayerGold -= 15
                Inventory.append("SpeedPotion")
            elif WhatDoYouWantToBuy == "longsword" and PlayerGold >= 30:
                print("\nYou bought a longsword")
                PlayerGold -= 30
                Inventory.insert(0, "Longsword")
                print("\nYou will automatically use this weapon in combat since it is your best one.")
            else:
                print("\nYou do not have enough money")
            
            print(f"\nYour inventory contains {Inventory} and you have {PlayerGold} gold")

def House():
    global PlayerHealth

    print("\nYou walk up the cobblestone pathway to your house. You enter your house and climb the stairs to your room.")
    Rest = input("\nDo you want to rest?\t")
    Rest = Rest.lower()

    if Rest == "yes":
        print("\nYou rest for a while.")

        PlayerHealth = PlayerHealth + 2
        print(f"\nYou are well rested(+2 health), your health is now {PlayerHealth} and ready for an adventure, so you go back to the town center.")

        TownCenter()
    else:
        print("\nYou decide you want to go back into the town center.")
        TownCenter()

def River():
    print("\nYou walk down the dirt pathway to the river. You hear the gushing of the water even before you see it. The path opens up to a river that is fast but fairly small.")

    if "Water" in Inventory:
        print("\nYou sit there for a while, but there is nothing for you to do here so you decide to leave and walk up the path back to the town center.")
        TownCenter()

    else:
        CollectWaterChoice = input("\nDo you want to collect water?\t")
        CollectWaterChoice = CollectWaterChoice.lower()

        if CollectWaterChoice == "yes":
            print("\nYou grab your extra flask and you fill it with the crystal clear water.(+Water)")
            Inventory.append("Water")

            print("\nYou enjoy the peace for a bit and then you go back to the town center.")
            TownCenter()
        else:
            print("\nYou stand there for a while, but you decide to head back to the town center.")
            TownCenter()

def DungeonEntrance():
    EnterDungeon = input("\nDo you want to enter the dungeon?(Yes/No)\t")
    EnterDungeon = EnterDungeon.lower()

    if EnterDungeon == "yes":
        print("\nYou enter the crypt by descending down the long winding staircase.")
        Room1()
    elif EnterDungeon == "no":
        print("\nYou decide that you aren’t ready and you go back to the village.")
        TownCenter()

def Room1():
    global Inventory
    print("\nYou enter a damp spacious room that has a big fountain in the middle. There is a plaque on the fountain that says ‘This fountain thirsts for the clear wine from the big river devine.")

    if "Water" in Inventory:
        PourWater = input("\nDo you want to pour the water into the fountain?(Yes/No)")
        PourWater = PourWater.lower()

        if PourWater == "yes":
            print("\nYou pour the crystal clear water into the fountain and nothing happens(-Water). Then you hear a bubbling noise as the fountain starts to run. You can now see there is an object at the bottom of the fountain. You reach into the water and you pull out a long sword.(+Longsword)")

            Inventory.remove("Water")
            Inventory.insert(0, "Longsword")
            print(f"\nYou will automatically use this weapon in combat since it is your best one. You have {Inventory} in your inventory.")

    print("\nYou can go to a chest room(Room 6), the coin room(Room 2), the combat(Room3), or go to town")
    Room1Direction = input("\nWhere do you want to go?(Room 6, Room 2, Room 3, Town)\t")
    Room1Direction = Room1Direction.lower()

    if Room1Direction == "room 6":
        Room6()
    if Room1Direction == "room 2":
        Room2()
    if Room1Direction == "room 3":
        Room3()
    if Room1Direction == "town":
        TownCenter()


def Room2():
    global PlayerGold
    global PlayerHealth
    if BeenToRoom2 == "No":
        BeenToRoom2 = "Yes"
        print("\nYou enter a strange empty room with little slits all over the wall on infront of you. You hear some gears start to turn and then coins start shooting out of the slits and the far end of the room. You try to dive to the ground to dodge the coins.")

        if PlayerSpeed > 10:
            print("\nYou dive to the ground and dodge all of the coins. You collect the coins off the ground.(+10 gold)")

            PlayerGold += 10
            print(f"\nYou now have {PlayerGold} gold.")
        
        else:
            print("\nYou were too slow and you get hit by some of the coins and then they evaporate into thin air.(-5 health)")

            PlayerHealth -= 5
            IsPlayerDead()
            print("\nYou are hurt but you are still okay, your health is PlayerHealth.")

            if "Health Potion" in Inventory:
                    UseHealhtPotion = input("\nDo you want to use a health potion?(Yes/No)\t")
                    UseHealhtPotion = UseHealhtPotion.loewr()

                    if UseHealhtPotion == "yes":
                        print("\nYou use a health potion.(+5 health, - health potion)")
                        PlayerHealth += 5

                        Inventory.remove("Health Potion")
                        print(f"\nYour health is now {PlayerHealth} and you have Inventory in your inventory.")
    print("\nYou can go to the fountain room(Room 1) or you can go to the chest room(Room 4)")
    Room2Direction = input("\nWhere do you want to go?(Room 1, Room 4)")
    Room2Direction = Room2Direction.lower()

    if Room2Direction == "room 1":
        Room1()
    elif Room2Direction == "room 4":
        Room4()

def Room3():
    global Room3Monster
    print("\nYou walk into the room and there is a bile of bones in the corner. You inspect them closer, then they come alive. Entering combat good luck.")
    Combat(Room3Monster)

    print("\nYou defeated the skeloton, now the room is empty.")
    print("\nYou can go to the fountain room(Room 1) or you can go to reward room(Room 5)")
    Room3Direction = input("\nWhere do you want to go?(Room 1, Room 5)\t")
    Room3Direction = Room3Direction.lower()

    if Room3Direction == "room 1":
        Room1()
    elif Room3Direction == "room 5":
        Room5()










def IsPlayerDead():
    global PlayerHealth
    if PlayerHealth > 0:
        return
    elif PlayerHealth <= 0:
        print("\nYou have died. The End.")








print("\nAn evil necromancer is living in the old crypt down just out of town. The village has grown worried, so they have picked you to fight him. You have some basic items that they have given you. Good luck.")
print("\nYou walk out of your house, down the cobblestone pathway, to the town center.")
TownCenter()