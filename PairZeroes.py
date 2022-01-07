def pair_zeros(arr):
    zero_found = False
    itr = 0
    while (itr != len(arr)):
        if arr[itr] == 0 and zero_found:
            arr.pop(itr)
            zero_found = False
            itr -= 1
        elif arr[itr] == 0:
            zero_found = True
        itr += 1
    return arr

print(pair_zeros([1,0,1,0,2,0,0]))