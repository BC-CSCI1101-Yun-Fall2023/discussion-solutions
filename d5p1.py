print("Welcome to your friendly ATM!")

balance = 1000.0

op = ""
while op != "quit":
    print(f"Current balance: ${balance:.2f}")
    op = input("What you want to do (deposit, withdraw, quit)? ")

    if op == "deposit":
        value = float(input("How much? $"))
        if value < 0:
            print(f"Can't {op} negative amounts!")
        else:
            balance += value
            
    elif op == "withdraw":
        value = float(input("How much? $"))
        if value < 0:
            print(f"Can't {op} negative amounts!")
        elif value > balance:
            print(f"Can't withdraw more than you have!")
        else:
            balance -= value
            
    elif op != "quit":
        print("Invalid operation!")

print(f"Final balance: ${balance:.2f}")
