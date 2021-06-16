def insertion_sort(lst: list) -> list:
    """Sort the given list in ascending order. Modifications are done in place

    Args:
        lst (list): List to be sorted

    Returns:
        list: Sorted list
    """
    for i in range(1, len(lst)):
        j = i - 1
        tmp = lst[i]

        while j >= 0 and tmp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = tmp

    return lst
