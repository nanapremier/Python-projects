import end as e

balance = 50000
PIN  = "1234"
attempts = 0

def x():
    pass

print("\033[36m=== WELCOME TO PYTHON BANK ===\033[0m")
while attempts < 3:
    try:
     entered = input("Enter your PIN: ")
    except ValueError:
     print("no latter writing here")
     continue
    if entered == PIN:
        print("PIN Correct. Welcome!")
        break
    else:
        print("Wrong PIN. Try again.")
        attempts += 1
else:
    print("Card Blocked!")
    exit()

while True:
    enum=["check balance","deposit","withdraw","exit"]
    for i, j in enumerate(enum, 1):
        print(f"{i}. {j}")
 
    choice = input("Choose 1-4: " ) 
    try:
        pass
    except:
        pass
    
    if choice == "1":
        print(f"Your balance is: {balance} FCFA")
    elif choice == "2":
        amt = float(input("Deposit amount: "))
        balance += amt
        print(f"Deposited {amt}. New balance: {balance}")
    elif choice == "3":
        amt = float(input("Withdraw amount: "))
        if amt > balance:
            print("Insufficient funds!")
        else:
            balance -= amt
            print(f"Withdrawn {amt}. New balance: {balance}")
    elif choice == "4":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice!")

print("Transaction history saved\nHave a nice day\nPython Bank v1.0")
e.end()