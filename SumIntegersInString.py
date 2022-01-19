def sum_of_integers_in_string(s):
    start = 0
    end = 0
    started = False
    sum = 0
    for i in range(len(s)):
        if s[i].isdigit() and started:
            end = i
        elif s[i].isdigit():
            start = i
            end = i
            started = True
        elif started:
            sum += int(s[start:end + 1])
            started = False
    if started:
        sum += int(s[start:])
    print(sum)

import re

def sum_of_integers_in_string2(s):
    return sum(int(x) for x in re.findall(r"(\d+)", s))

tests = ['12.4', '2 + 3 =']
for x in tests:
    sum_of_integers_in_string(x)