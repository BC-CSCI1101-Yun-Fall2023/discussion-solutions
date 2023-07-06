import string
import sys

def do_translation(word):
    if word[0] in "aeiou":
        pig = word + "way"
    else:
        for i,char in enumerate(word):
            if char in "aeiouy":
                break
        pig = word[i:]+word[:i]+"ay"
    return pig

def word_to_pig_latin(word):
    for first_letter,char in enumerate(word):
        if char not in string.punctuation:
            break
    for last_letter,char in enumerate(word[::-1]):
        if char not in string.punctuation:
            break
    last_letter = len(word)-last_letter
    actual_word = word[first_letter:last_letter]

    pig = do_translation(actual_word.lower())

    if word.istitle():
        pig = pig.title()

    pig = word[:first_letter]+pig+word[last_letter:]
    return pig

def file_to_pig_latin(original, pig):
    for line in original:
        words = line.split()
        for word in words:
            pig_latin = word_to_pig_latin(word)
            print(pig_latin, end=" ", file=pig)
        print(file=pig)

in_filename = input("Enter the input file name: ")
out_filename = input("Enter the output file name: ")

try: 
    with (
        open(in_filename) as in_file,
        open(out_filename, "w") as out_file,
    ): 
        file_to_pig_latin(in_file, out_file)  
except IOError: 
    print(f"File Error!") 
    sys.exit()
