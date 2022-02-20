def series_sum(n):
    denom = 1
    ans = 0
    for x in range(n):
        ans += (1 / denom)
        denom += 3
    return (format(ans, '.2f'))

series_sum(1)