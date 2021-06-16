def binary_search(arr: list, target: int) -> int:
    """Uses binary search algorithm to search the given array for a given element. Returns index of the element if found and -1 otherwise

    Args:
        arr (list): Sorted array
        target (int): Element to look for in the given array

    Returns:
        int: Index of the element if found, -1 otherwise
    """
    min_idx, max_idx = 0, len(arr) - 1
    while min_idx <= max_idx:
        mid_idx = min_idx + (max_idx - min_idx) // 2
        if arr[mid_idx] == target:
            return mid_idx
        elif arr[mid_idx] > target:
            max_idx = mid_idx - 1
        else:
            min_idx = mid_idx + 1
    return -1
