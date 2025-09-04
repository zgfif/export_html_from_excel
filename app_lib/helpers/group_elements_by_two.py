def group_elements_by_two(lst: list) -> list[tuple[str, str]]:
    """
    Receives a list like: ['abc', 'cde', 'fhi', 'jkl', 'lmn', 'opq'] and
    returns a new list with paired elements [('abc', 'cde'), ('fhi', 'jkl'), ('lmn', 'opq')].
    The input list must have an even number of elements.
    Raises:
        ValueError: If the length of the list is odd.
    """
    paired_lst = []

    if len(lst) % 2 != 0:
        raise ValueError('The list must have an even count of elements.')

    for i in range(0, len(lst), 2):
        paired_lst.append((lst[i], lst[i+1]))
    
    return paired_lst
