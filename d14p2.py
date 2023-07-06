import math
import sys

def is_float(word):
    try:
        f = float(word)
    except ValueError:
        return False
    return True

def get_values(data_file):
    values = []
    for line in data_file:
        words = line.strip().split()
        for word in words:
            if not is_float(word):
                continue
            values.append(float(word))
    values.sort()
    return values
            
def get_mean(vals):
    return sum(vals)/len(vals)

def get_median(vals):
    mid = int(len(vals) / 2)
    if len(vals) % 2 == 0:
        return (vals[mid-1]+vals[mid])/2
    return vals[mid]

def get_stddev(vals):
    sqdiffs = 0
    mean = get_mean(vals)
    for val in vals:
        sqdiffs += (mean-val)**2
    return math.sqrt(sqdiffs/len(vals))

def get_modes(vals):
    counts = {}
    for val in vals:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
    max_count = max(counts.values())
    modes = []
    for val,count in counts.items():
        if count == max_count:
            modes.append(val)
    return modes

in_filename = input("Enter the input file name: ")

try: 
    with open(in_filename) as in_file: 
        values = get_values(in_file)
except IOError: 
    print(f"Error with {in_filename}!") 
    sys.exit()

if len(values) == 0:
    print(f"No values in {in_filename}.")
    sys.exit()

print(f"Min: {values[0]:.3f}")
print(f"Max: {values[-1]:.3f}")
print(f"Mean: {get_mean(values):.3f}")
print(f"Median: {get_median(values):.3f}")
modes = get_modes(values)
print("Mode: ", end="")
for mode in modes:
    print(f"{mode:.3f} ", end="")
print()
print(f"Standard Deviation: {get_stddev(values):.3f}")


    
