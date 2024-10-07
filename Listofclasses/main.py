#Sawyer Wood, List of classes skill practice.
class1 = input("What is your 1st class?")
class2 = input("What is your next class?")
class3 = input("What is your next class?")
class4 = input("What is your next class?")
class5 = input("What is your next class?")
class6 = input("What is your next class?")
class7 = input("What is your next class?")
class8 = input("What is your next class?")

classes = []

classes.append(class1)
classes.append(class2)
classes.append(class3)
classes.append(class4)
classes.append(class5)
classes.append(class6)
classes.append(class7)
classes.append(class8)

place = 0
length = len(classes)

print("Your classes are", classes)
while place <= length - 1:
    print("Your", (place + 1), "class is", classes[place])
    place = place + 1