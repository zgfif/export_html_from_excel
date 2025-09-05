def group_elements_by_two(items: tuple[str, ...]) -> tuple[tuple[str, str], ...]:
    """
    Receives a tuple like: ('abc', 'cde', 'fhi', 'jkl', 'lmn', 'opq') and
    returns a new tuple with paired elements (('abc', 'cde'), ('fhi', 'jkl'), ('lmn', 'opq')).
    The input tuple must have an even number of elements.
    Raises:
        ValueError: If the length of the tuple is odd.
    """

    if len(items) % 2 != 0:
        raise ValueError(f"Expected even number of elements, got {len(items)}")

    return tuple(zip(items[::2], items[1::2]))
