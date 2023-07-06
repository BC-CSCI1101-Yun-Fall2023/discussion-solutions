def merge_lists(list1, list2):
    merged = []
    if len(list1) >= len(list2):
        merged = list1.copy()
        for i,value in enumerate(list2):
            merged[i] = merged[i] + value
    else:
        merged = list2.copy()
        for i,value in enumerate(list1):
            merged[i] = value + merged[i]
    return merged

firsts = ["Peggy", "Natasha","Bruce", "Thor"]
lasts = ["Carter", "Romanoff", "Banner"]
fulls = merge_lists(firsts,lasts)
print(fulls)

vals_a = [1, 2]
vals_b = [1, 2, 3, 4]
vals_c = merge_lists(vals_a, vals_b)
print(vals_c)

test1a = []
test1b = []
test1merged = merge_lists(test1a, test1b)
print(test1merged)
        
