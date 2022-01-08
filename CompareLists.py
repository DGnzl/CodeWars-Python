def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    for x in array1:
        if x**2 not in array2:
            return False
        array2.remove(x**2)
    return len(array2) == 0

def comp2(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False