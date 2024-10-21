#Sawyer Wood, count up and down skill practice.
counter = 1

goalnum = int(input("What is the number you want to count to?: "))
for x in range(goalnum):
    print(x)
else:
    print(goalnum)

for x in range(goalnum):
    print(goalnum - counter)
    counter = counter + 1