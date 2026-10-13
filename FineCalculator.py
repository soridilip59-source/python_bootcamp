
def calculate_fine(late_days, book_type="standard", premium=False):
    if late_days <= 0:
        fine = 0

    elif book_type == "standard":
        if late_days <= 5:
            fine = late_days * 5
        else:
            fine = (5 * 5) + ((late_days - 5) * 10)

    elif book_type == "reference":
        fine = late_days * 20

    else:
        print("Invalid book type!")
        return None

    # Apply 20% discount for premium members
    if premium:
        fine = fine * 0.80

    return fine


# Test cases
print(calculate_fine(3))
print(calculate_fine(8))
print(calculate_fine(4, "reference"))
print(calculate_fine(8, "standard", True))
print(calculate_fine(4, "reference", True))
print(calculate_fine(0))
