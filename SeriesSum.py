def series_sum(n):
    denom = 1
    for x in range(n - 1):
        n += (1 / denom)
        denom += 3
    return str(round(n ,2))