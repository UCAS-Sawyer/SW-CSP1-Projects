#Sawyer Wood, error handlins calculator skill practice.


while True:

    def stop_pls(stop):
        stop.lower()
        if stop == "stop":
            return True

    num1 = input("Number one: ")
    if stop_pls(num1) == True:
        break
    operation = input("What operation do you want use?(+, -, *, /): ")
    if stop_pls(operation) == True:
        break
    num2 = input("Number two: ")
    if stop_pls(num2) == True:
        break
    
    try:
        num1 = int(num1)
        num2 = int(num2)
        print(num1, operation, num2, "=")

    except:
        print("Invalid numbers.")
        continue

    if operation in ["+", "-", "*", "/"]:
        pass
    else:
        print("Invalid operation.")
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operation == "+":
        num3 = num1 + num2
        print(num3)

    else:
        if operation == "-":
            num3 = num1 - num2
            print(num3)

        else:
            if operation == "*":
                num3 = num1 * num2
                print(num3)
            
            else:
                if operation == "/":
                        num3 = num1 / num2
                        print(num3)