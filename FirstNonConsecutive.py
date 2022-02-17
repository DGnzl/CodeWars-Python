def first_non_consecutive(arr):
    for x in range(len(arr) - 1):
        if arr[x] + 1 != arr[x + 1]:
            return arr[x + 1]
    return None