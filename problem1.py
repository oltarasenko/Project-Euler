"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
"""


def is_multuply_by_three_five(value):
    """
    Returns true if value is multiply by three or five
    >>> is_multuply_by_three_five(15)
    True
    >>> is_multuply_by_three_five(11)
    False
    """
    if value % 3 == 0 or value % 5 == 0:
        return True
    return False


def sum(limit):
    """
    Prints a sum of all values multipliable by three or five
    below the limit
    """
    sum = 0
    for x in range(0, limit):
        if is_multuply_by_three_five(x):
            sum += x
    return sum

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print sum(1000)
    # 233168
