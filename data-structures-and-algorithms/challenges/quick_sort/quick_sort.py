def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if end >= start:
        j = start
        for i in range(start, end):
            if arr[i] < arr[end]:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        arr[j], arr[end] = arr[end], arr[j]

        quick_sort(arr, start, j - 1)
        quick_sort(arr, j + 1, end)

    return arr
