age = int(input("Enter your age: "))

gender = input("Enter your gender (male/female): ")

traveling_alone = input("Are you traveling alone? (yes/no): ") == "yes"

tatkal = input("Are you booking a Tatkal ticket? (yes/no): ") == "yes"

blackout_holiday = input("Is it a blackout festival holiday? (yes/no): ") == "yes"


eligible = (
    (age >= 60 or (gender == "female" and traveling_alone))
    and not tatkal
    and not blackout_holiday
)

print(eligible)