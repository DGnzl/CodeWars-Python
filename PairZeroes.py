def pair_zeros(arr):
    zero_found = False
    test = []
    for i in range(len(arr)):
        if arr[i] == 0 and zero_found:
            arr.pop(i)
            zero_found = False
        elif arr[i] == 0:
            zero_found = True
    return arr

print(pair_zeros([1, 2, 0, 3, 0]))