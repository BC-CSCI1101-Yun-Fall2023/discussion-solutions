import sys

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def get_positive_int(name):
    value = int(input(f"Enter {name}: "))
    if value <= 0:
        print(f"{name} must be positive!")
        sys.exit()
    return value

input1 = get_positive_int("a")
input2 = get_positive_int("b")

gcd_result = gcd(input1, input2)

print(f"The GCD is {gcd_result}.")
