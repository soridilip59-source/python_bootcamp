def total_spent(expenses):
    """Return the total amount spent."""

    total = 0

    for item, amount in expenses:
        total += amount

    return total


def biggest_expense(expenses):
    """Return the tuple with the highest amount."""

    if not expenses:
        return None

    sorted_expenses = sorted(
        expenses,
        key=lambda expense: expense[1]
    )

    return sorted_expenses[-1]