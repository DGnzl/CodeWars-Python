def find_short(s):
    ans = 100
    for x in s.split(' '):
        ans = min(ans, len(x))
    return ans
    # return min(len(x) for x in s.split())