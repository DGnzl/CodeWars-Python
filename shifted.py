def shifted_diff(first, second):
    fw = list(first)
    for x in range(len(first)):
        if ''.join(fw) == second:
            return x
        fw.insert(0, fw.pop())
    return -1

print(shifted_diff('eecoff', 'coffee'))
print(shifted_diff('  ', ' '))