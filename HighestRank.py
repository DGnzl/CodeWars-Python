def highest_rank(arr):
    print(arr)
    highest_count = 0
    highest_value = 0
    for i in set(sorted(arr)):
        curr_count = arr.count(i)
        if curr_count > highest_count:
            highest_count = curr_count
            highest_value = i
        elif curr_count == highest_count and i > highest_value:
            highest_value = i
    return highest_value