def key_of_longest_value(my_dict):
    if len(my_dict) == 0:
        return None
    
    longest_value_key = None
    for key,value in my_dict.items():
        if longest_value_key == None:
            longest_value_key = key
    
        if len(value) > len(my_dict[longest_value_key]):
            longest_value_key = key

    return longest_value_key

maps = {"a": "12345",
        "b": "1234",
        "c": "123"}
print(key_of_longest_value(maps))

maps = {"a": "123",
        "b": "12345",
        "c": "123"}
print(key_of_longest_value(maps))

maps = {"a": "123",
        "b": "123",
        "c": "1234"}
print(key_of_longest_value(maps))

maps = {"a": "123"}
print(key_of_longest_value(maps))

maps = {}
print(key_of_longest_value(maps))
