def find_uniq(arr):
    key = 0
    if (arr[0] == arr[1]):
        for x in arr:
            if x != arr[0]:
                return x
    else:
        if arr[0] == arr[2]:
            return arr[1]
        else:
            return arr[0]

def small_change():
    pass