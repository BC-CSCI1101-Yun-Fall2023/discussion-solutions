import sys

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

def remove_punctuation(s):
    clean = ""
    for char in s:
        if char.isalnum():
            clean += char
    return clean

def is_palindrome(s):
    s = remove_punctuation(s.lower())
    if s == reverse_string(s):
        return True
    return False

print("Enter some text to check for palindromes, quit to stop: ")

for line in sys.stdin:
    line = line.strip()
    if line.lower() == "quit":
        break
    if is_palindrome(line):
        print("That's a palindrome!")
    else:
        print("Nope.")
