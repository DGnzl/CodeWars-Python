def unused_digits(*args):
    return "".join(number for number in "0123456789" if number not in str(args))

print(unused_digits([12, 34, 56, 78]))