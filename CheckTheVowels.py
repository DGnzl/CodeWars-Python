def sort_vowels(s):
    if not isinstance(s, str): 
        return ''
    ans = []
    for c in s:
        if c.lower() in ('a','e', 'i','o','u'):
            ans.append(f'|{c}')
        else:
            ans.append(f'{c}|')
    return '\n'.join(ans)