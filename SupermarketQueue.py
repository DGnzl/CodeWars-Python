def queue_time(customers, n):
    tills = [0] * n
    itr = 0
    total_time = 0
    while itr < len(customers):
        if tills.count(0) > 0:
            tills[tills.index(0)] = customers[itr]
            itr += 1
        else:
            remove_shortest = min(tills)
            total_time += remove_shortest
            for x in range(n):
                tills[x] -= remove_shortest
    total_time += max(tills)
    print(total_time)

def queue_time2(customers, n):
    tills = [0] * n
    for x in customers:
        tills[0] += x
        tills.sort()
    print(tills[-1])

queue_time2([2,2,3,3,4,4], 2)
queue_time2([22, 20, 28, 11, 25, 6, 50, 17, 28, 20, 22, 47, 22, 8, 50, 7, 35, 11], 4)