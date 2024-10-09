#Sawyer Wood, shopping list manager proficiency test.

list = []

def removeaction1():
    print("You chose to remove a specfic item. This is your lise currently", list)
    item = input("What item do you want to remove?: ")
    list.remove(item)
    print(list)

def removeaction2():
    print("You chose to remove a specfic item spot This is your lise currently", list)
    itemspot = int(input("What spot do you want to remove?: "))
    list.pop(itemspot)
    print(list)

def add():
    addeditem = input("What item would you like to add?: ")
    list.append(addeditem)
    print(list)

while True:


    action = int(input("""What would you like to do?

                        Enter 1 to add item

                        Enter 2 to remove item

                        Enter 3 to leave the list
                   
                        Enter 4 to see your list\n"""))

    if action == 1:

        add()

    elif action == 2:
        removeaction = int(input("You could remove a specified item or you could remove a certain item spot. Which one do you want to do 1 or 2?"))

        if removeaction == 1:

            removeaction1()

        elif removeaction == 2:
            
            removeaction2()

    elif action == 3:

        print("Have a nice day!")

        break

    elif action == 4:
        print(list)