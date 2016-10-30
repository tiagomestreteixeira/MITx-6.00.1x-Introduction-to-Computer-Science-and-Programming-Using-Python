def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def base_multiplier(base):
        total = 0
        for idx in range(len(L)):
            multiplier = base ** (len(L) - idx - 1)
            total += L[idx] * multiplier
        return total

    return base_multiplier


print(general_poly([1, 2, 3, 4])(8))
