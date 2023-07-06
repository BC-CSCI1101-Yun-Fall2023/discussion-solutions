import sys

def analyze_file(content):
    lines = 0
    words = 0
    chars = 0
    for line in content:
        lines += 1
        chars += len(line)
        words += len(line.split())
    return lines, words, chars

in_filename = input("Enter the input file name: ")

try: 
    with open(in_filename) as in_file: 
        lines,words,chars = analyze_file(in_file)  
except IOError: 
    print(f"Error with {in_filename}!") 
    sys.exit()

print(f"# Lines: {lines}")
print(f"# Words: {words}")
print(f"# Chars: {chars}")
