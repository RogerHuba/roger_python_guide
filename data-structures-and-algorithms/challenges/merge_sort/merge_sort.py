def merge(L: list, R: list, lst: list) -> list:
    """Merge 2 lists sorting them in ascending orders

    Args:
        L (list): list one
        R (list): list two
        lst (list): resulting list

    Returns:
        list: merged list sorted asc
    """
    i = j = k = 0

    while i < len(L) and j < len(R):

        if L[i] < R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1

    if i < len(L):
        lst[k:] = L[i:]
    elif j < len(R):
        lst[k:] = R[j:]

    return lst


def merge_sort(lst: list) -> list:
    """Sort a list in ascending order (modification is done in-place)

    Args:
        lst (list): list to be sorted

    Returns:
        list: same list, but sorted
    """
    _len = len(lst)

    if _len > 1:
        mid_idx = _len // 2
        L = lst[0: mid_idx]
        R = lst[mid_idx:]

        merge_sort(L)
        merge_sort(R)

        merge(L, R, lst)

    return lst
