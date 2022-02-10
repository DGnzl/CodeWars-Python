def same_case(a, b):
    if a.isalpha() and b.isalpha():
        return a.isupper() == b.isupper()
    return -1