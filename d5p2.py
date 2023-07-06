import random
import math

count = 15
vals = []
while len(vals) < count:
    vals.append(random.uniform(0,100))

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
