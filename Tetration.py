def tetration(x, y):
    if y == 0:
        return 1
    ans = x
    for z in range(y - 1):
        ans = x ** ans
    return ans