import sys

def get_word_counts():   
    words = {}
    print("Enter words, each on their own line, Ctrl-D to stop:")
    for word in sys.stdin:
        word = word.strip().lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

def find_max_count(words):
    if len(words) == 0:
        return None
    most_used = None
    for word,count in words.items():
        if most_used == None:
            most_used = word
        elif count > words[most_used]:
            most_used = word
    return most_used

counts = get_word_counts()
most_used = find_max_count(counts)
if most_used == None:
    print("No words entered.")
else:
    print(f"The most used word was '{most_used}'.")
