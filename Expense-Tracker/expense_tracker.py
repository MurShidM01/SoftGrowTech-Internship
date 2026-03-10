# Personal Expense Tracker (Beginner Version)

FILE_NAME = "expenses.txt"


# Function to add expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    expense = date + "," + category + "," + amount + "," + description + "\n"

    file = open(FILE_NAME, "a")
    file.write(expense)
    file.close()

    print("Expense added successfully!\n")


# Function to view expenses
def view_expenses():
    try:
        file = open(FILE_NAME, "r")
        expenses = file.readlines()
        file.close()

        print("\n--- Expense List ---")
        for exp in expenses:
            data = exp.strip().split(",")
            print("Date:", data[0],
                  "| Category:", data[1],
                  "| Amount:", data[2],
                  "| Description:", data[3])
        print()

    except:
        print("No expenses found.\n")


# Function to calculate total
def total_expenses():
    total = 0

    try:
        file = open(FILE_NAME, "r")
        expenses = file.readlines()
        file.close()

        for exp in expenses:
            data = exp.strip().split(",")
            total = total + float(data[2])

        print("Total Expenses:", total, "\n")

    except:
        print("No expenses found.\n")


# Main menu
while True:

    print("====== Personal Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Program Closed.")
        break

    else:
        print("Invalid choice\n")