pennies = int(input("Enter the number of pennies: "))

dollars = int(pennies/100)
cents = pennies % 100

print(f"That is ${dollars}.{cents:02d}.")
