def oddTuples(aTup):
    """
    aTup: a tuple

    returns: tuple, every other element of aTup.
    """
    new_tuple = ()
    for i in range(0, len(aTup)):
        if i % 2 == 0:
            new_tuple += (aTup[i],)

    return new_tuple


print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
