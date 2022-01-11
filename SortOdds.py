def sort_array(source_array):
    # source_array = []
    _temp = []
    for i in source_array:
        if i % 2 == 1:
            _temp.append(i)
    _temp.sort()
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = _temp.pop(0)
    return source_array

print(sort_array([5, 3, 2, 8, 1, 4]))