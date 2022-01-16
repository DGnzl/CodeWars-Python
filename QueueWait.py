def queue(queuers,pos):
    tix = queuers[pos]
    count = tix
    for x in queuers[0 : pos]:
        count += min(x, tix)
    for x in queuers[pos + 1:]:
        count += min(x, tix - 1)
    print(count)

queue([2, 5, 3, 6, 4], 1)