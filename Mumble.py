def accum(s):
    copies = 1
    ans = []
    for x in s:
        sentence = f'{x.upper()}{x.lower() * (copies - 1)}'
        ans.append(sentence)
        copies += 1
    return '-'.join(ans)