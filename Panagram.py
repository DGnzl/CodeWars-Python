import string

def is_pangram(s):
    return 26 == len(set([x for x in s.lower() if x.isalpha()]))

is_pangram("The quick, brown fox jumps over the lazy dog!")