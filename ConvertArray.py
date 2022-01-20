def digitize(n):
    ans = []
    while n > 0:
        ans.append(n % 10)
        n = n // 10
    if len(ans) == 0:
        ans.append(n)
    return ans