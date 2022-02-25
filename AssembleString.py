def assemble(arr):
    ans = list(arr[0]) if arr else []
    arr_len = len(arr)
    for x in range(len(ans)):
        cursor = 0
        while cursor < arr_len and ans[x] == '*':
            if arr[cursor][x] != '*':
                ans[x] = arr[cursor][x]
            cursor += 1
    return ''.join(ans).replace('*', '#')

assemble(['H*llo, W*rld!', 'Hel*o, *or*d!', '*ello* World*'])
assemble(['******', '******', '******', '******'])