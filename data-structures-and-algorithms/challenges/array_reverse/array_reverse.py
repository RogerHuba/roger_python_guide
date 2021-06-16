def reverse_array(lst):
    """Function that reverses a given array

    Arguments:
        lst {lst} -- Python list

    Returns:
        lst -- Python list
    """
    output = []
    for _ in range(len(lst)):
        output.append(lst.pop())
    return output


def reverse_array_in_place(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[-i - 1] = lst[-i - 1], lst[i]
    return lst
