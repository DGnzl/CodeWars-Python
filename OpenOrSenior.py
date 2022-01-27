def open_or_senior(data):
    ans = []
    for x in data:
        if x[0] > 54 and x[1] > 7:
            ans.append('Senior')
        else:
            ans.append('Open')
    return ans

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
