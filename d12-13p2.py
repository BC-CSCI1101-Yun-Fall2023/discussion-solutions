import sys

def get_range(content):
    nums = []
    for line in content:
        words = line.strip().split()
        for word in words:
            nums.append(float(word))
    if len(nums) == 0:
        return None,None

    nums.sort()
    return nums[0], nums[-1]

in_filename = input("Enter the input file name: ")

try: 
    with open(in_filename) as in_file: 
        min_value,max_value = get_range(in_file)  
except IOError: 
    print(f"Error with {in_filename}!") 
    sys.exit()

if min_value == None:
    print(f"No values in {in_filename}!")
else:
    print(f"[{min_value},{max_value}]")
