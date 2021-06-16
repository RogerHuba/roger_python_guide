def get_max_area(histogram: list) -> int:
    stack = []
    max_area = 0
    length = len(histogram)

    for curr_idx, curr_el in enumerate(histogram):
        new_idx = curr_idx
        while len(stack) > 0 and stack[-1][1] > curr_el:
            prev_idx, prev_el = stack.pop()
            max_area = max(max_area, (curr_idx - prev_idx) * prev_el)
            new_idx = prev_idx
        stack.append((new_idx, curr_el))

    while len(stack) > 0:
        prev_idx, prev_el = stack.pop()
        max_area = max(max_area, (length - prev_idx) * prev_el)

    return max_area