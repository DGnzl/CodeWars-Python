def f(s):
    second_index = s.find(s[0], 1)
    if second_index == -1 or len(s) % second_index != 0:
        return (s, 1)
    return (s[:second_index], len(s) // second_index)