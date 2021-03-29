def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''
    if c is None:
        add = 1
    else:
        add = c
    if not b:
        current = 0
        place = 0
        while place < a:
            yield current
            current += add
            place += add
    else:
        current = a
        while current < b:
            yield current
            current += add
