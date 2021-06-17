def spin_words(sentence):
    lst = sentence.split()
    index = 0
    for word in lst:
        if len(word) > 4:
            lst[index] = word[::-1]
        index += 1
    return " ".join(lst)