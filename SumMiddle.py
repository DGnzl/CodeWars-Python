def sum_array(arr):
    return 0 if (arr is None or len(arr) == 0) else sum(sorted(arr)[1:-1])