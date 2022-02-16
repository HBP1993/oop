# from CellPhoneClass import CellPhone

# my_manufact = input("Enter the name of manufacturer: ")

# my_model = str(input("Enter the model number: "))

# my_retail_price = float(input("Enter the retail price: "))

# CellPhone = CellPhone(my_manufact, my_model, my_retail_price)
# print(f"Name is {my_manufact}.")
# print(f"Model is {my_model}.")
# print(f"Retail price is ${my_retail_price}.")

import CellPhoneClass as cp

my_CellPhone = cp.CellPhone('Apple', '13ProMAx', '1299')


print("Name is", my_CellPhone.get_manufact())
print("Model is", my_CellPhone.get_model())
print("Retail price is", my_CellPhone.get_retail_price())