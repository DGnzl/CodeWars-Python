def longest(a1 , a2):
    hash = set(a1 + a2)
    return ''.join(sorted(list(hash)))

# return ''.join(sorted(set(a1 + a2))

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))