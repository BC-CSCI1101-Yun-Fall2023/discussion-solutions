import sys

count = int(input("How many numbers do you have? "))
if count <= 0:
    print("Need at least one number!")
    sys.exit()

nums = []
i = 1
print(f"Enter the {count} numbers each on their own line:") 
while i <= count:
    nums.append(float(input()))
    i += 1

pos_count = 0
zero_count = 0
neg_count = 0
for num in nums:
    if num > 0:
        pos_count += 1
    if num == 0:
        zero_count += 1
    if num < 0:
        neg_count += 1

pos_percent = pos_count / count * 100
zero_percent = zero_count / count * 100
neg_percent = neg_count / count * 100

print(f"{pos_percent:.2f}% positive values.")
print(f"{zero_percent:.2f}% zero values.")
print(f"{neg_percent:.2f}% negative values.")

