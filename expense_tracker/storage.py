import csv


FILE_NAME = "expenses.csv"


def save_expenses(expenses):
    # Save all expenses to a CSV file.

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Item", "Amount"]
        )

        # Write the CSV header
        writer.writeheader()

        # Write each expense tuple
        for item, amount in expenses:
            writer.writerow({
                "Item": item,
                "Amount": amount
            })


def load_expenses():
    # Load expenses from CSV and return a list of tuples

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            expenses = []

            for row in reader:
                item = row["Item"]
                amount = int(row["Amount"])

                expenses.append((item, amount))

            return expenses

    except FileNotFoundError:
        # If the CSV does not exist yet, start with an empty list
        return []
