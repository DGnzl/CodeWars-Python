def get_count(sentence):
    vowels = ['a','e','i','o','u']
    sentence.lower()
    count = 0
    for v in vowels:
        count += sentence.count(v)
    return count