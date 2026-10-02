# FASTag Highway Toll Tax Calculator

vehicle_type = input("Enter vehicle type (car/bus/truck): ")
fastag_active = input("Is FASTag active? (yes/no): ") == "yes"
is_national_holiday = input("Is today a national holiday? (yes/no): ") == "yes"

if not fastag_active:
    print("Double toll penalty applied: cash mode")

else:
    if is_national_holiday:
        print("Holiday toll rate applies.")
    else:
        print("Regular toll rate applies.")