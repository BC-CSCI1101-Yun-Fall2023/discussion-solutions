import sys

def is_int(word):
    try:
        i = int(word)
    except ValueError:
        return False
    return True

def is_float(word):
    try:
        f = float(word)
    except ValueError:
        return False
    return True

def split_file(inf, ints, floats, strs):
    for line in inf:
        words = line.strip().split()
        for word in words:
            if is_int(word):
                print(word, file=ints)
            elif is_float(word):
                print(word, file=floats)
            else:
                print(word, file=strs)

in_filename = input("Enter the input file name: ")
int_filename = input("Enter the integer output file name: ")
float_filename = input("Enter the float output file name: ")
str_filename = input("Enter the string output file name: ")

try: 
    with (
        open(in_filename) as in_file,
        open(int_filename, "w") as int_file,
        open(float_filename, "w") as float_file,
        open(str_filename, "w") as str_file,
    ): 
        split_file(in_file, int_file, float_file, str_file)  
except IOError: 
    print(f"File Error!") 
    sys.exit()


