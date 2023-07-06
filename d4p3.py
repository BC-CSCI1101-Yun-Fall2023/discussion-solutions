import sys

n = int(input("Enter n: "))

if n < 1:
    print("n must be at least 1!")
    sys.exit()

i = 1
while i <= n:
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if output == "":
        output = i

    print(output)

    i += 1

