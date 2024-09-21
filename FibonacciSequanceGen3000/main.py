#Sawyer Wood, Fibonacci Sequance RAID.

Origin1 = 0
Origin2 = 1
num1 = Origin1
num2 = Origin2
HowManyTimes = int(input("How many unmbers do you want?: "))
HowManyTimes = HowManyTimes - 2
Count = 0
print(num1)

while Count <= HowManyTimes:
    Count = Count + 1
    Current = num1 + num2
    print(Current)
    num1 = num2
    num2 = Current