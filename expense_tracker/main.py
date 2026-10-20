from storage import save_expenses, load_expenses
from reports import total_spent, biggest_expense


def main():
    expenses = load_expenses()

    print("===== EXPENSE TRACKER =====")

    for i in range(3):
        try:
            item = input("Enter expense item: ").strip()

            if item == "":
                print("Item cannot be empty.")
                continue

            amount = int(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            expenses.append((item, amount))

        except ValueError:
            print("Please enter a valid number.")

    save_expenses(expenses)

    print("\n===== EXPENSE REPORT =====")

    for item, amount in expenses:
        print(f"{item}: ₹{amount}")

    print(f"\nTotal spent: ₹{total_spent(expenses)}")

    biggest = biggest_expense(expenses)

    if biggest:
        print(
            f"Biggest expense: {biggest[0]} "
            f"- ₹{biggest[1]}"
        )
    else:
        print("No expenses found.")


if __name__ == "__main__":
    main()