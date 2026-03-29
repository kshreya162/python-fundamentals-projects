expenses=[]    #List of dictionaries of expenses

print("Welcome to Expense Tracker")


while True:
    print("\n========== MENU  ==========")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. Total expenses")
    print("4. Exit")
    print("=============================")

    choice=int(input("Enter your choice(1-4) :"))

#ADD EXPENSES
    if choice == 1:
        date=input("Enter date (dd-mm-yyyy): ")
        category = input("Enter category(Food, Travel, Shopping etc) : ")
        description=input("Enter short decsription: ")
        amount= float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!!")

#VIEW EXPENSES
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses!!")
        else:
            count=1
            for item in expenses:
                print(f"number {count}\nDate of expenditure: {item['date']}\nCategory: {item['category']} \nDescription:{item['description']} \nAmount: {item['amount']}")
                count+=1

#view total spending
    elif choice==3:
        total=0
        for item in expenses:
            total+=item['amount']
        print("\nTotal expenditure:", total)

#exit
    elif choice==4:
        print("Thank you!!!")
        break
    else:
        print("Enter the valid number")
