#4fun
import random
money = 100
prize1 = 5
prize2 = 15
prize3 = 30
prize4 = 70
prize5 = 145
jackpot = 300
casinogain = 0
while money > 0:
    spin = input("Spin?: ")
    if spin == str("Yes"):
        money = money - 15
        casinogain = casinogain + 15
        num = random.randint(0,100)
        print("You rolled", num)
        if num <= 50:
            money = money + prize1
            casinogain = casinogain - prize1
            print("You won", prize1, "dollors!")
            
        if 75 >= num > 50:
            money = money + prize2
            casinogain = casinogain - prize2
            print("You won", prize2, "dollors!")

        if 87 >= num > 75:
            money = money + prize3
            casinogain = casinogain - prize3
            print("You won", prize3, "dollors!")

        if 93 >= num > 87:
            money = money + prize4
            casinogain = casinogain - prize4
            print("You won", prize4, "dollors!")
        
        if 99 >= num > 93:
            money = money + prize5
            casinogain = casinogain - prize5
            print("You won", prize5, "dollors!")
        
        if num == 100:
            money = money + jackpot
            casinogain = casinogain - jackpot
            print("You won", jackpot, "dollors!")
    print("You currently have", money, "dollors and the casino has made",casinogain, "dollors!")