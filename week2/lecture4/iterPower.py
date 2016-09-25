def iter_power(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    total = 1.0000
    for i in range(1, exp + 1):
        total *= base

    return total


print(iter_power(7.83, 5))
