import math
import sys

op = input("Enter log, ln, or log2: ")
val = float(input("Enter a value: "))

if op == "log":
    result = math.log10(val)
elif op == "ln":
    result = math.log(val)
elif op == "log2":
    result = math.log2(val)
else:
    print("That's not a valid operation!")
    sys.exit()

print(f"{op}({val:.3f}) = {result:.3f}")
