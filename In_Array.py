def in_array(array1, array2):
    ans = set()
    for x in array1:
        for y in array2:
            if x in y:
                ans.add(x)
                break
    print(ans)
    return sorted(list(ans))
            