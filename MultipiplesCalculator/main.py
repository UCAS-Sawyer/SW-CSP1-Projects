#Sawyer Wood, multiplication table proficiency test.

num = int(input("What number do you want to find the multiples of?: "))
amount = int(input("How many multiples do you want?: "))

print(f"{amount} multiples of {num} are: ")

for x in range(amount + 1):

    multiple = num * x
    print(f"\t{multiple}")