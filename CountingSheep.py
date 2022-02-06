def count_sheeps(sheep):
    ans = []
    return len([x for x in sheep if x is True])

# Notable solution
def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)