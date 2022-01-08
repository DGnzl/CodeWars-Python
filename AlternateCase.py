def alternate_case(s):
    ans = ''
    for c in s:
        if c.isupper():
            ans+= c.lower()
        else:
            ans += c.upper()
    return ans

def alternate_case2(s):
    return s.swapcase()