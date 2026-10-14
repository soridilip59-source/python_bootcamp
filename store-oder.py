
Prices = {
    "apple": 20,
    "banana": 10,
    "milk": 30,
    "bread": 25,
    "eggs": 50
}

out_of_stock = {"banana", "eggs"}

Order = ["apple", "banana", "milk", "bread", "eggs"]

total = 0

for item in Order:
    if item in out_of_stock:
        print(item, "is unavailable")
    else:
        total += Prices[item]

print("Final order value:", total)
