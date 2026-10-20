from storage import save_expenses, load_expenses
from reports import total_spent, biggest_expense


def main():
    # 1. Purane expenses file se load karo
    expenses = load_expenses()

    print("EXPENSE TRACKER")
    print(f"Previously saved expenses: {len(expenses)}")

    # 2. User se 3 naye items aur amounts lo
    for i in range(1, 4):
        print(f"\nEnter expense {i}")

        item = input("Enter item name: ").strip()
        amount_input = input("Enter amount (₹): ").strip()

        # 3. Invalid amount ko friendly message ke saath skip karo
        try:
            amount = int(amount_input)

            if amount <= 0:
                raise ValueError

        except ValueError:
            print("Invalid amount. This expense will be skipped.")
            continue

        expenses.append((item, amount))
        print("Expense added successfully!")

    # 4. Poori list (purani + nayi) save karo
    save_expenses(expenses)

    # 5. Total aur biggest expense print karo
    print("\nEXPENSE REPORT")
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
