#Sawyer Wood, password validator skill practice.

password = input("What is the password that you want to check?:\t")

def passwordnum(x):
    lenx = len(x)
    counter = 0
    while counter < lenx:
        if password[counter] == int:
            return True
        
        if password[counter] != int:
            counter = counter + 1

def passwordspec(x):
    lenx = len(x)
    counter = 0
    while counter < lenx:
        if password[counter] != str or int:
            return True
        
        if password[counter] == str or int:
            counter = counter + 1
        
#Condition 1
while len(password) < 8:
    print("You need a longer password(8 Characters), try again.")
    password = input("What is the password that you want to check?:\t")
else:
    print("\nThat is enough characters.")

#Condition 2
while passwordnum(password) == False:
    print("You need a number, try again.")
    password = input("What is the password that you want to check?:\t")
else:
    print("\nYou have a number.")

#Condition 3
while passwordspec(password) == False:
    print("You need a special character, try again.")
    password = input("What is the password that you want to check?:\t")

else:
    print("\nYour password is good.\n")
