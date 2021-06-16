def join(ht_1: dict, ht_2: dict, option: str = 'left') -> dict:
    """Join 2 hash tables

    Args:
        ht_1 (dict): Hash table 1
        ht_2 (dict): Hash table 2
        option (str, optional): Left or right join. Defaults to 'left'.

    Returns:
        dict: Joined hash table
    """
    if option == 'right':
        ht_1, ht_2 = ht_2, ht_1

    output = {}

    for key in ht_1:
        val = ht_2[key] if key in ht_2 else None
        output[key] = (ht_1[key], val)

    return output
