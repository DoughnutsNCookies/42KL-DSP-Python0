def ft_filter(function, iterable) -> list:
    """
        Return an iterator yielding those items of iterable
        for which function(item) is true.
        If function is None, return the items that are true.
    """
    if function is None:
        return iterable
    return [x for x in iterable if function(x)]
