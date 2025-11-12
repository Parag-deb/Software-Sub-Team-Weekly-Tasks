app_name = "CLI Expense Tracker"
expenses = []
def show_menu():
    """Displays the menu options"""
    print(f"\n {app_name}")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Delete Expense")
    print("5. Search Expense by Category")
    print("6. Exit")

def add_expense(category, amount, note=""):
    global expenses
    expenses.append({
        "category": category,
        "amount": amount,
        "note": note
    })
    print(f"Added expense: {category} - {amount:.2f} Taka")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nExpense List:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - {exp['amount']:.2f} Taka ({exp['note']})")

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expense: {total:.2f} Taka")
    return total


def delete_expense(index):
    try:
        removed = expenses.pop(index)
        print(f"🗑️ Deleted: {removed['category']} - {removed['amount']:.2f} Taka")
    except IndexError:
        print("Invalid expense number!")

def search_by_category(category):
    found = [exp for exp in expenses if exp["category"].lower() == category.lower()]
    if not found:
        print(f"No expenses found in '{category}' category.")
    else:
        print(f"\n{category.capitalize()} Expenses: ")
        for exp in found:
            print(f"- {exp['category']} - {exp['amount']:.2f} Taka ({exp['note']})")

def expense_tracker():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            category = input("Enter expense category: ").capitalize()
            try:
                amount = float(input("Enter amount (Taka): "))
                note = input("Enter a short note (optional): ")
                add_expense(category, amount, note)
            except ValueError:
                print("Please enter a valid number for amount!")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            view_expenses()
            try:
                index = int(input("Enter expense number to delete: ")) - 1
                delete_expense(index)
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "5":
            category = input("Enter category name to search: ").capitalize()
            search_by_category(category)

        elif choice == "6":
            print("\nSaving and exiting... tata!")
            break

        else:
            print("Invalid choice! Please select between 1-6.")


if __name__ == "__main__":
    try:
        expense_tracker()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting safely.")