def gcd_iter(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print(gcd_iter(9, 12))
