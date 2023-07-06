import sys

def check_perfect(n):
    i = 1
    total = 0
    while i < n:
        if n % i == 0:
            total += i
        i += 1
    if total == n:
        return True
    return False

def get_positive_int(name):
    value = int(input(f"Enter {name}: "))
    if value <= 0:
        print(f"{name} must be positive!")
        sys.exit()
    return value

value = get_positive_int("N")
if check_perfect(value):
    print(f"{value} is a perfect number!")
else:
    print(f"{value} is not a perfect number.")
