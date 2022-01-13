def up_array(arr):
    if len(arr) == 0:
        return None
    for i in arr:
        if i > 9 or i < 0:
            return None
    idx = 1
    while (idx <= len(arr) and arr[-idx] == 9):
        arr[-idx] = 0
        idx += 1
    if idx <= len(arr):
        arr[-idx] += 1
    else:
        arr.insert(0, 1)
    return arr
    
print(up_array([2,3,9]))
print(up_array([1,-9]))
print(up_array([9,9,9]))
print(up_array([]))