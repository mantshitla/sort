def merge_sort_by_length(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort_by_length(items[:mid])
    right = merge_sort_by_length(items[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Original (ascending) if left[i] == right[j]
        # Modified (longest first)
        if len(left[i]) >= len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result