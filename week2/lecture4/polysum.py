from math import *


def polysum(n, s):
    """
    :param n: number of sides
    :param s: length of each side
    :return: sum of : - the area and the square of the perimeter
    """
    perimeter_squared = (n * s) ** 2
    area = (0.25 * n * s ** 2) / tan(pi / n)
    return round(perimeter_squared + area, 4)
