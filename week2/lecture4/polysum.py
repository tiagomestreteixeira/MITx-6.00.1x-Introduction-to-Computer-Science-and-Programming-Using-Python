import math


def polysum(n, s):
    """
    :param n: number of sides
    :param s: length of each side
    :return: sum of the are and square of the perimeter
    """
    perimeter_squared = (n * s) ** 2
    area = (0.25 * n * s * s) / (math.tan(math.pi / n))
    return round(perimeter_squared + area, 4)
