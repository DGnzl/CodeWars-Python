import re

def order(sentence):
    ans = dict()
    for w in sentence.split():
        ans[int(re.sub("[^0-9]", "", w))] = w
    return ' '.join([ans[x] for x in sorted(ans.keys())])

print(order("is2 Thi1s T4est 3a"))