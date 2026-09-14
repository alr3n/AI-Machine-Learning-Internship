# Simple Expense Tracker

import sys

# Support UTF-8 symbols on Windows terminals
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

# Expense categories
CATEGORIES = [
    "Food",
    "Transportation",
    "School",
    "Bills",
    "Entertainment",
    "Shopping",
    "Other",
]


# Format number as currency (₱)
def format_peso(amount):
    return f"₱{amount:,.2f}"


# Print header title
def print_header(title):
    print()
    print("=" * 10 + " " + title + " " + "=" * 10)
    print()


# Get description from user
def ask_for_description():
    while True:
        description = input("Enter expense description: ").strip()

        if description == "":
            print("Description cannot be empty.")
            print("Please type something like 'Lunch'.\n")
        else:
            return description


# Get amount from user
def ask_for_amount():
    while True:
        user_input = input("Enter amount: ")

        # Check if input is a valid number
        try:
            amount = float(user_input)
        except ValueError:
            print("Invalid amount.")
            print("Please enter a valid number.\n")
            continue

        # Check if amount is greater than 0
        if amount <= 0:
            print("Amount must be greater than zero.\n")
            continue

        return amount


# Let user choose a category
def ask_for_category():
    print("\nChoose a category:")

    # Show category options
    for number, category in enumerate(CATEGORIES, start=1):
        print(f"  {number}. {category}")

    while True:
        user_input = input("Enter category number: ")

        # Validate number
        try:
            choice = int(user_input)
        except ValueError:
            print("Invalid choice. Please enter a number.\n")
            continue

        # Check if choice is valid
        if 1 <= choice <= len(CATEGORIES):
            return CATEGORIES[choice - 1]

        print(f"Please enter a number between 1 and {len(CATEGORIES)}.\n")


# Add a new expense
def add_expense(expenses):
    print_header("ADD EXPENSE")

    description = ask_for_description()
    amount = ask_for_amount()
    category = ask_for_category()

    # Create expense dictionary
    expense = {
        "description": description,
        "amount": amount,
        "category": category,
    }

    # Add expense to list
    expenses.append(expense)

    print("\n\u2713 Expense added successfully!")


# View all recorded expenses
def view_expenses(expenses):
    print_header("EXPENSE HISTORY")

    # Check if empty
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    # Display each expense
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']}")
        print(f"   Category: {expense['category']}")
        print(f"   Amount: {format_peso(expense['amount'])}")
        print()


# Calculate total of all expenses
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


# Display total spending summary
def show_total(expenses):
    print_header("EXPENSE SUMMARY")

    # Check if empty
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    total = calculate_total(expenses)

    print(f"Number of Expenses: {len(expenses)}")
    print(f"Total Spending: {format_peso(total)}")


# Calculate total spending per category
def build_category_totals(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] = category_totals[category] + amount
        else:
            category_totals[category] = amount

    return category_totals


# Display spending summary by category
def category_summary(expenses):
    print_header("CATEGORY SUMMARY")

    # Check if empty
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    category_totals = build_category_totals(expenses)

    # Align columns neatly
    longest_name = max(len(category) for category in category_totals)
    label_width = longest_name + 2

    # Print each category total
    for category in category_totals:
        label = category + ":"
        print(f"{label:<{label_width}} {format_peso(category_totals[category])}")

    print()
    total_label = "Total:"
    print(f"{total_label:<{label_width}} {format_peso(calculate_total(expenses))}")


# Display the main menu
def show_menu():
    print()
    print("=" * 40)
    print("          SIMPLE EXPENSE TRACKER")
    print("=" * 40)
    print()
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Category Summary")
    print("5. Exit")
    print()


# Main program function
def main():
    # List to store expenses
    expenses = []

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            print("\nThank you for using Simple Expense Tracker. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


# Run the program
if __name__ == "__main__":
    main()
