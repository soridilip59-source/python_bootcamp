from storage import save_expenses, load_expenses
from reports import total_spent, biggest_expense


def get_item_name():
    """Tab tak poochta hai jab tak item ka naam khaali na ho."""

    while True:
        item = input("Enter item name: ").strip()

        if item:
            return item

        print("Item name khaali nahi ho sakta. Dobara try karo.")


def get_valid_amount():
    """Tab tak poochta hai jab tak sahi (positive) amount na mile."""

    while True:
        amount_input = input("Enter amount (₹): ").strip()

        try:
            amount = int(amount_input)

            if amount <= 0:
                raise ValueError

            return amount

        except ValueError:
            print("Invalid amount. Please enter a positive number.")


def main():
    # Purane saved expenses load karo
    expenses = load_expenses()

    print("EXPENSE TRACKER")
    print(f"Previously saved expenses: {len(expenses)}")

    # 3 naye expenses lo
    for i in range(1, 4):
        print(f"\nEnter expense {i}")

        item = get_item_name()
        amount = get_valid_amount()

        expenses.append((item, amount))
        print("Expense added successfully!")

    # Purane + naye, sab save karo
    save_expenses(expenses)

    # Report dikhao
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
