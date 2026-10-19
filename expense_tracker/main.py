from storage import save_expenses, load_expenses
from reports import total_spent, biggest_expense


def main():
    # Load previously saved expenses
    expenses = load_expenses()

    print("=== EXPENSE TRACKER ===")
    print(f"Previously saved expenses: {len(expenses)}")

    # Ask the user to enter three new expenses
    for i in range(1, 4):
        print(f"\nEnter expense {i}")

        item = input("Enter item name: ").strip()

        # Keep asking until a valid amount is entered
        amount_input = input("Enter amount (₹): ").strip()

        try:
            amount = int(amount_input)

            if amount <= 0:
                raise ValueError

        except ValueError:
            print("Invalid amount. This expense will be skipped.")
            continue

        # Add the valid expense to the existing list
        expenses.append((item, amount))

        print("Expense added successfully!")

    # Save the entire list, including old and new expenses
    save_expenses(expenses)

    # Display reports
    print("\n=== EXPENSE REPORT ===")

    print(f"Total expenses: ₹{total_spent(expenses)}")

    biggest = biggest_expense(expenses)

    if biggest is not None:
        item, amount = biggest
        print(f"Biggest expense: {item} — ₹{amount}")
    else:
        print("No expenses recorded yet.")

    print("\nAll expenses:")

    for item, amount in expenses:
        print(f"{item}: ₹{amount}")


if __name__ == "__main__":
    main()