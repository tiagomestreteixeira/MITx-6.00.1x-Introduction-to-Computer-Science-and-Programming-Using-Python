def f(a, b):
    return a + b


def dict_interdiff(d1, d2):
    """
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    """
    keys_in_both = {}
    keys_difference = {}
    for key_d1 in d1.keys():
        if key_d1 in d2.keys():
            keys_in_both[key_d1] = f(d1[key_d1], d2[key_d1])
        else:
            keys_difference[key_d1] = d1[key_d1]

    for key_d2 in d2.keys():
        if key_d2 not in d1.keys():
            keys_difference[key_d2] = d2[key_d2]

    return keys_in_both, keys_difference


d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}

print(dict_interdiff(d1, d2))
