def number(bus_stops):
    ans = 0
    for x in bus_stops:
        ans += x[0] - x[1]
    return ans