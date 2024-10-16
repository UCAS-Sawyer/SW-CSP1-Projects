#Sawyer Wood, What is my grade skill practice.
counter = 0
print("(Skip lunch)")

while counter < 7:
    counter += 1
    classname = input("What is the name of this class?: ")
    percent = input("What is your percent in this class?: ")

    if counter == 1:
        class1 = f" Your grade for {classname} is {percent}%,"

    elif counter == 2:
        class2 = f" your {classname} grade is {percent}%,"

    elif counter == 3:
        class3 = f" your {classname} grade is {percent}%,"

    elif counter == 4:
        class4 = f" your {classname} grade is {percent}%,"

    elif counter == 5:
        class5 = f" your {classname} grade is {percent}%,"

    elif counter == 6:
        class6 = f" v{classname} grade is {percent}%,"

    elif counter == 7:
        class7 = f" your {classname} grade is {percent}%,"

print(class1, class2, class3, class4, class5, class6, class7)