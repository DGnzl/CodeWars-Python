from re import X


def filter_list(l):
    return [x for x in l if type(x) is int]