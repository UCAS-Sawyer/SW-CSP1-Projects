#Sawyer Wood, Fibonacci Sequance RAID.

Origin1 = 0
Origin2 = 1
HowManyTimes = int(input("How many unmbers do you want?: "))
HowManyTimes = HowManyTimes - 2
Count = 0
print(Origin1)

while Count <= HowManyTimes:
    Count = Count + 1
    Current = Origin1 + Origin2
    print(Current)
    Origin1 = Origin2
    Origin2 = Current