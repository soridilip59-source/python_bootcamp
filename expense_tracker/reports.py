def total_spent(expenses):
    total = 0

    for item, amount in expenses:
        total += amount

    return total


def biggest_expense(expenses):
    if not expenses:
        return None

    biggest = expenses[0]

    for expense in expenses:
        if expense[1] > biggest[1]:
            biggest = expense

    return biggest