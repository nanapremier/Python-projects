expenses = []

def add_expense():
    name = input("What did you buy? e.g. Rice: ")
    try:
          amount = float(input("How much? e.g. 2000: "))
    except ValueError:
          print("please enter a NuMBER for amount.Expense not add.")
          return
    if amount <= 0:
        print("amount must be more than 0.")
        return
    category = input("Category? e.g. Food, Transport, School: ")

    expense = {"name": name, "amount": amount, "category": category}
    expenses.append(expense)
    print("Expense added!")

def show_expenses():
    print("\n--- Your Expenses ---")
    for e in expenses:
        print(f"{e['name']} - {e['amount']} FCFA - {e['category']}")

def show_total():
    total = 0
    for e in expenses:
        total += e['amount']
    print(f"\nTotal spent: {total} FCFA")
def show_total_by_category():
    print("\n--- Total by Category ---")
    totals = {}
    for e in expenses:
        cat = e['category']
        if cat in totals:
            totals[cat] += e['amount']
        else:
            totals[cat] = e['amount']
    
    for cat, total in totals.items():
        print(f"{cat}: {total} FCFA")    

while True:
    enum=["add expense","show expense","show total","Exit"]
    for i,j in enumerate(enum,1):
        print(f"{i}.{j}")
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid choice")
