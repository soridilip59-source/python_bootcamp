# student={"dilip","kumar","singh","amit","kumar"}

# is_exist = "ramesh" in student


# print(is_exist)
# if is_exist:
#     print(student)
# else:
#     student.add("ramesh")
#     print(student)
 


inventory={ "Rice":50,"soap":20,"sugar":30,"salt":10}

# reduce the count of rice by 2
inventory["Rice"] -= 2
print(inventory)

input_item = input("Enter the item : ")
if input_item in inventory:
    inventory[input_item] += 1
    print(inventory)
else:
    inventory[input_item] = 10
    print(inventory)