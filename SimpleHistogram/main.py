#Sawyer Wood, Simple Histogram RAID

typeo = input("Do you want to input each one individually or a list?\t")

if typeo in ["i", "I", "Individually", "individually"]:

    while True:
        number = int(input("\nWhat number do you want to turn into a visual representation:\t"))

        for x in range(number):
            print("*", end = "")

        if number == "S":
            break

if typeo in ["l", "L", "list", "List"]:
    numberline = str(input("List all the numbers(No spaces, can only do 0-9):\t"))
    for x in numberline:
        x = int(x)
        print("\n")
        for y in range(x):
            print("*", end = "")