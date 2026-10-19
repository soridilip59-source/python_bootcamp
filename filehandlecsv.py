import csv

contacts= [
    {"Name": "Amit","Phone":"9875636512"},
    {"Name": "Dilip","Phone":"9875236512"},
    {"Name": "Sakshi","Phone":"9775636512"},
    {"Name": "Sunita","Phone":"9175636512"},
    {"Name": "Dinesh","Phone":"9075636512"}
]

with open("contacts.csv","w", newline="") as file:
    fieldnames = ["Name","Phone"]
    writer= csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(contacts)

with open("contacts.csv","r",newline="") as file:
    reader = csv.DictReader(file)
    for contact in reader:
        if contact["Name"].startswith("S"):
            print(contact["Name"],contact["Phone"])