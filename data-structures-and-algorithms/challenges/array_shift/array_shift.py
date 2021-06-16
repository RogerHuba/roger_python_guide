def insertShiftArray(lst, el):
    """Function that inserts given element into the middle of the given array

    Arguments:
        lst {lst} -- List to be modifyed
        el {Any} -- Element to be inserted

    Returns:
        lst -- List with the inserted element
    """
    l = len(lst)
    if l % 2:
        mid = l // 2 + 1
    else:
        mid = l // 2
    return lst[:mid] + [el] + lst[mid:]
