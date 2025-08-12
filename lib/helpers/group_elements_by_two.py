def group_elements_by_two(lst: list) -> list:
    """Receives a list like: ['abc', 'cde', 'fhi', 'jkl', 'lmn', 'opq'] and
    Returns a new list with paired elements [['abc', 'cde'], ['fhi', 'jkl'], ['lmn', 'opq']]"""
    paired_lst = []

    if len(lst) % 2 != 0:
        raise ValueError('The list must has even count of elements.')

    for i in range(len(lst) - 1):
        if i % 2 == 0:
            paired_lst.append([lst[i], lst[i+1]])
        if i == len(lst) - 2:
            break

    return paired_lst