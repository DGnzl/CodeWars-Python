def nb_year(p0, percent, aug, p):
    ans = 0
    percent /= 100
    while (p0 < p):
        ans += 1
        p0 += int(p0 * percent) + aug
    return ans