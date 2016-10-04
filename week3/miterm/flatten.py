def flatten(aList):
    """
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    """
    new_list = []
    if type(aList) == list:
        for i in aList:
            new_list += list(flatten(i))
    else:
        new_list += [aList]
    return new_list


L = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(L))
# [1,'a','cat',2,3,'dog',4,5]
print(L)
