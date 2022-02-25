def remove_smallest(numbers):
    copy = list(numbers)
    if copy:
        copy.remove(min(copy))
    return copy

print(remove_smallest([1, 2, 3, 4, 5]))