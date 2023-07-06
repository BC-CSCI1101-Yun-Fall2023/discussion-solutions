def check_sorted(values):
    if len(values) == 0:
        return True
    last_value = values[0]
    for value in values:
        if last_value > value:
            return False
        last_value = value
    return True

test1 = []
print(check_sorted(test1))

test2 = [1]
print(check_sorted(test2))

test3 = [1, 2, 3]
print(check_sorted(test3))

test4 = [1, 1, 1]
print(check_sorted(test4))

test5 = [1, 0]
print(check_sorted(test5))

test6 = [1, 2, 3, 4, 3]
print(check_sorted(test6))

test7 = [1, 0, 2, 3, 4, 3]
print(check_sorted(test7))
