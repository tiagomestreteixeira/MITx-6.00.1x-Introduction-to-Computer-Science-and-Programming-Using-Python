def recur_power(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    if exp == 0:
        return 1.0000
    else:
        return base * recur_power(base, exp - 1)


print(recur_power(7.83, 5))
