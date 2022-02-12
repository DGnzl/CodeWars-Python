def duplicate_count(text):
    d = dict()
    for s in text:
        s = s.lower()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return len([x for x in d.values() if x > 1])

duplicate_count("Indivisibilities")