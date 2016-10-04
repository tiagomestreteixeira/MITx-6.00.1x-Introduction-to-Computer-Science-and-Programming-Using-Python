def dotProduct(listA, listB):
    """
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    """
    total = 0
    for i in range(0, len(listA)):
        total += listA[i]*listB[i]
    return total

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(dotProduct(list1,list2))
