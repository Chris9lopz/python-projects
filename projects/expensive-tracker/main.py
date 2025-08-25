# Import built-in function from data.py
from data import add_expense, list_expenses, total_expenses, export_to_csv

# Define list of expenses
expenses = []

# Menu options
print("""
What would you like to do?
1. Add Expense
2. List Expenses
3. Total Expenses
4. Export to CSV
5. Quit
""")

# Loop while option is selected
while True:

    # User option
    option = int(input("\nEnter choice: "))

    # Selected option by user with match
    match option:
        case 1:
            # 1. Request description product and amount
            description = input("Description: ")
            amount = float(input("Amount: "))
            # 2. Add to expenses
            expenses.append(add_expense(description=description, amount=amount))
            # 3. Send updated status to user
            print("Added!")
        case 2:
            # Show description products
            print("Expenses:")
            print(list_expenses(expenses))
        case 3:
            # Calculate total expenses function
            print(total_expenses(expenses=expenses))
        case 4:
            filename = input("Enter filename: ")
            list_of_expenses = list_expenses(expenses)
            export_to_csv(filename, list_of_expenses)
        case 5:
            print("Goodbye!")
            break
