def xo(s):
    ans = {'x':0, 'o':0}
    for x in s:
        if x.lower() in ('x','o'):
            ans[x.lower()] += 1
    return ans['x'] == ans['o']

def xo2(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo2('xxoOOX'))
print(xo('Xxoo'))