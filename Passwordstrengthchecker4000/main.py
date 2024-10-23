#Sawyer Wood, password validator skill practice.

import re

def passwordnum(password):
    for x in password:
        if x.isdigit():
            return True
    return False

def passwordspec(password):
    pattern = r'[!@#$%^&*(),.?":{}|<>]'
    return bool(re.search(pattern, password))

while True:    
    password = input("What is the password that you want to check?:\t")

    #Condition 1
    if len(password) < 8:
        print("You need a longer password(8 Characters), try again.\n")
        continue
    else:
        print("\nThat is enough characters.\n")

    #Condition 2
    if passwordnum(password) == False:
        print("Please add a number, try again.\n")
        continue
    else:
        print("You have a number.\n")

    #Condition 3
    if passwordspec(password) == False:
        print("Please add a special character, try again.\n")
        continue
    else:
        print("Your password is good.\n")
        break