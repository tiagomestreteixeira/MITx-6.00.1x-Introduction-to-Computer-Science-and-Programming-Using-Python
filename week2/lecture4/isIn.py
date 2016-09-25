def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) == 0:
        return False

    if len(aStr) == 1:
        return char == aStr[0]

    if aStr[int(len(aStr) / 2)] == char:
        return True

    if char < aStr[int(len(aStr) / 2)]:
        return isIn(char, aStr[:int(len(aStr) / 2)])
    else:
        return isIn(char, aStr[int(len(aStr) / 2):])
