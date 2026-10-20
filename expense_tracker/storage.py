import csv
import os

FILE_NAME = "expenses.csv"


def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Item", "Amount"])

        for item, amount in expenses:
            writer.writerow([item, amount])


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    expenses = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            item = row["Item"]
            amount = int(row["Amount"])

            expenses.append((item, amount))

    return expenses