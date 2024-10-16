#Sawyer Wood, Authorized proficiency test.

adminlist = ["Sawyer"]
authorizedlist = ["John", "Sam", "Sky", "Bob", "Kal", "Carl", "Penny", "Owen"]

name = input("What is your name? \nInput Name Here -->  ")

if name in adminlist:
    print(f"\nWelcome Back Admin: \n\t{name}\n")

elif name in authorizedlist:
    print(f"\nWelcome Authorized Personel: \n\t{name}\n")

else:
    print(f"\n{name} Is Not An Authorized Name, Please Get Authorization From Admin.\n")