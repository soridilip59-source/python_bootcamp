import csv

FILE_NAME = "expenses.csv"


def save_expenses(expenses):
    """Expenses ko CSV mein save karta hai.

    Header row: Item, Amount
    Har (item, amount) tuple ke liye ek row.
    """

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Item", "Amount"])

        # Header row likho
        writer.writeheader()

        # Har tuple ke liye ek row likho
        for item, amount in expenses:
            writer.writerow({"Item": item, "Amount": amount})


def load_expenses():
    """CSV se expenses padhta hai (DictReader se).

    (item, amount) tuples ki list return karta hai, amount int mein.
    File na ho to crash kiye bina [] return karta hai.
    """

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            expenses = []

            for row in reader:
                item = row["Item"]
                amount = int(row["Amount"])  # text ko int banao
                expenses.append((item, amount))

            return expenses

    except FileNotFoundError:
        # File abhi bani nahi, to khaali list
        return []


# ---- Test: 2 expenses save karke expenses.csv check karo ----
# Is file ko seedha chalane par hi ye test chalega
# (main.py se import karne par nahi chalega).
if __name__ == "__main__":
    save_expenses([("Chai", 20), ("Auto", 80)])
    print("Saved! Ab expenses.csv file khol kar check karo.")
    print("Loaded:", load_expenses())
