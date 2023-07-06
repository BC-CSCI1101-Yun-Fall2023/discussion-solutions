def lists2dict(keys, values):
    merged = {}
    for index,key in enumerate(keys):
        if index >= len(values):
            merged[key] = None
        else:
            merged[key] = values[index]
    return merged

letters = ["A", "B", "C"]
phonetics = ["alpha", "bravo", "charlie"]
military = lists2dict(letters, phonetics)
print(military)

letters = ["A", "B", "C", "D"]
phonetics = ["alpha", "bravo", "charlie"]
military = lists2dict(letters, phonetics)
print(military)

letters = ["A", "B", "C"]
phonetics = ["alpha", "bravo", "charlie", "delta"]
military = lists2dict(letters, phonetics)
print(military)
