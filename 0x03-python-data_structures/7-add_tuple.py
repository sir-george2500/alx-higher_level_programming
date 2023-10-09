def add_tuple(tuple1, tuple2):
    """
    Add two tuples element-wise.

    Args:
        tuple1: First tuple.
        tuple2: Second tuple.

    Returns:
        A new tuple containing the sum of corresponding elements.
    """
    return tuple(x + y for x, y in zip(tuple1, tuple2))
