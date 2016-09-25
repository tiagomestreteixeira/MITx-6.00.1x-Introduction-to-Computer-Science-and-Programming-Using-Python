def gcd_recur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    if a == b:
        return a
    if a > b:
        return gcd_recur(a - b, b)
    else:
        return gcd_recur(a, b - a)


print(gcd_recur(9, 12))
