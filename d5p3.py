import random
import math
import sys

count = int(input("How many random numbers? "))
if count < 1:
    print("Need at least one number!")
    sys.exit()
    
lower_bound = float(input("Lower bound? "))
upper_bound = float(input("Upper bound? "))

vals = []
while len(vals) < count:
    vals.append(random.uniform(lower_bound,upper_bound))

mean = 0
for val in vals:
    mean += val
mean /= count

diffs = 0
for val in vals:
    diffs += (val-mean)**2

std_dev = math.sqrt(diffs/count)

print(f"Mean = {mean:.3f}")
print(f"Standard Deviation = {std_dev:.3f}")
