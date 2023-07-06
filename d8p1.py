import sys

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

print("Enter some text, quit to stop: ")

for line in sys.stdin:
    line = line.strip()
    if line.lower() == "quit":
        break
    print(reverse_string(line))
