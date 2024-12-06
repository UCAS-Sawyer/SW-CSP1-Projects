#Sawyer Wood, Simple Histogram RAID

Counter = 0

typeo = input("Do you want to input each one individually or a list?\t")

if typeo in ["i", "I", "Individually", "individually"]:

    while True:
        number = int(input("\nWhat number do you want to turn into a visual representation:\t"))

        for x in range(number):
            print("*", end = "")

        if number == "S":
            break

if typeo in ["l", "L", "list", "List"]:
    x = 0
    list1 = []
    amount = int(input("How many numbers are going to be in the list?\t"))
    while x < amount:
        x += 1
        position = int(input("Give one number in the list, left to right.\t"))
        list1.append(position)
    else:
        for x in list1:
            x = int(x)
            print("\n")
            Counter += 1
            print(f"{Counter}:")
            for y in range(x):
                print("*", end = "")