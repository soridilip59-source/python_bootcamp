def total_spent(expenses):
    """List mein saare expenses ke amounts ka sum return karta hai."""

    total = 0

    for item, amount in expenses:
        total += amount

    return total


def biggest_expense(expenses):
    """Sabse zyada amount wala (item, amount) tuple return karta hai.

    sorted() ke saath lambda key use karke amount nikaala gaya hai.
    List khaali ho to None return karta hai.
    """

    if not expenses:
        return None

    # lambda expense: expense[1]  ->  tuple ka amount
    sorted_expenses = sorted(expenses, key=lambda expense: expense[1])

    # Sort ke baad sabse last wala sabse bada hota hai
    return sorted_expenses[-1]
