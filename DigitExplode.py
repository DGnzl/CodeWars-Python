def explode(s):
    ans = ''
    for d in s:
        ans += d * int(d)
    return ans

def explode2(s):
    return ''.join(d * int(d) for d in s)

print(explode2('321'))