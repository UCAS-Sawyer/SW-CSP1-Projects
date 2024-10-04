#sawyer Wood, comments froficiency test.

class BankAccount: #setting class to BankAccount
    def __init__(self, account_number, balance=0): #define __init__ function
        self.account_number = account_number #setting the variable account_number
        self.balance = balance #setting the variable balance

    def deposit(self, amount): #define deposit function
        if amount > 0: #if you are adding money
            self.balance += amount #Adds "amount" of money to your balance
            return True
        return False

    def withdraw(self, amount):#define withdraw function
        if 0 < amount <= self.balance: #if the amount of money you're taking is greater than zero, but is less or equal to the amount of money you
            self.balance -= amount #take "amount" of money out
            return True
        return False

    def get_balance(self):#define get_balance function
        return self.balance #return the amount of money you have

def create_account():#define create_account function
    account_number = input("Enter account number: ") #Asking for acount number
    initial_balance = float(input("Enter initial balance: ")) #Asking for howmuch money you have in it
    return BankAccount(account_number, initial_balance) #Return accoutn number and balance

def main():#define main function
    accounts = {}
    while True:
        print("\n1. Create Account") #print option 1
        print("2. Deposit") #print option 2
        print("3. Withdraw") #print option 3
        print("4. Check Balance") #print option 4
        print("5. Exit") #print option 5
        
        choice = input("Enter your choice (1-5): ") #asking what you want to do
        
        if choice == '1': #if they chose 1
            account = create_account() #Calling the create account function
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!") #print what it did
        
        elif choice in ['2', '3', '4']: #If they chose 2-4
            account_number = input("Enter account number: ") #asking for your account number
            if account_number in accounts: #If the program can find the account number.
                account = accounts[account_number]
                if choice == '2': #If they chose 2
                    amount = float(input("Enter deposit amount: ")) #ask how much they are depositing
                    if account.deposit(amount): #call the deposit function
                        print(f"Deposited ${amount:.2f} successfully!") #print what it did
                    else:
                        print("Invalid deposit amount.") #if you are adding a invalid amount
                elif choice == '3': #If they chose 3
                    amount = float(input("Enter withdrawal amount: ")) #ask how much they are withdrawing
                    if account.withdraw(amount): #call the withdraw function
                        print(f"Withdrawn ${amount:.2f} successfully!") #print what it did
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")  #If they can't withdraw that amount
                else:
                    print(f"Current balance: ${account.get_balance():.2f}") #if they chose 4, call get_balance function, print their balance
            else:
                print("Account not found.") #If the program can't finde the accout number
        
        elif choice == '5': #if they chose 5
            print("Thank you for using our banking system. Goodbye!") #print goodbye
            break #stop the program
        
        else:
            print("Invalid choice. Please try again.") #if they chose something not from 1 to 5

if __name__ == "__main__": #If __name__ is the same as string "__main__"
    main() #call main function